# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 16:32:27 2017

@author: AlexH
"""

#Priors 1: state, number


#Updates & Results: state, time, number

#Step 1, get all data (use just website time info for now)

#Step 2, rolling regression

#Step 3, find error margin at each stage

#Step 4, compare with financial data
    

import numpy as np
import csv
import matplotlib.pyplot as plt
from sklearn import linear_model, datasets
import statsmodels.api as sm

import pandas as pd
from collections import OrderedDict
from datetime import date

from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pylab

#%%
#Reading in data


with open('prior-538.csv', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    prior=list(data)

prior = pd.DataFrame(prior)
prior.columns = ['State', 'poll', 'EV']


#with open('call-AP.csv', newline='') as csvfile:
#    data = csv.reader(csvfile, delimiter=',')
#    call=list(data)
#
#call = pd.DataFrame(call)
#call.columns = ['State', 'result', 'time']

with open('results.csv', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    result=list(data)

result = pd.DataFrame(result)
result.columns = ['State', 'result', 'time', 'trump', 'clinton', 'diff', 'intermediate','rprpc']


#join the table by state
jointb = prior.join(result.set_index('State'), on='State')
#order by time


#remove empty rows
jointb['EV'].replace('#N/A', np.nan, inplace=True)
jointb.dropna(subset=['EV'],inplace=True)

jointb = jointb.sort_values(by='time').reset_index(drop=True)
jointb.index = np.arange(0,len(jointb))
jointb[['poll', 'EV','result', 'trump', 'clinton', 'diff']]=jointb[['poll', 'EV','result', 'trump', 'clinton', 'diff']].apply(pd.to_numeric)



#%%
#Assume we know the perent difference
#http://www.bbc.com/news/world/us_and_canada/states/dc

#storing result
columns = ['time', 'state','low', 'ave', 'high']
index= jointb.index
pred=pd.DataFrame(index=index, columns=columns)

#number of simulation for (a,b) and (error)
sim_num = 200
for i in range(3,len(jointb)-6):
    
    #fit linear regression
    select=jointb[0:i].drop_duplicates(subset='State', keep='last')
    X=select['poll'][0:i]
    Y=select['diff'][0:i]
    X=sm.add_constant(X)
    model = sm.OLS(Y, X).fit()
    
    #extract parameters
    const = np.random.normal(model.params[0], model.bse[0], sim_num)
    slope = np.random.normal(model.params[1], model.bse[1], sim_num)
    
    #make predictions, use states with no results and intermediate results
    remain=jointb[~jointb.State.isin(select.State)].drop_duplicates(subset='State', keep='last')
    for j in range(0, len(const)):
        error = np.random.normal(np.mean(model.resid), np.std(model.resid), sim_num)
        result = np.array([v + const[j] + slope[j]*remain['poll'] for v in error])
        result = result>0
        result = result.astype(int)
        
    #filling the result of intermediates states with current count
    select.result[select.result.isnull()[0:i]]=(select['diff'][select.result.isnull()[0:i]]>=0).astype(int)
    
    EEV=sum(select['result'][0:i] * select['EV'][0:i])+ np.dot(result, remain['EV'])
#    print(jointb['time'][i],jointb['State'][i], EEV)

    #make table for plot
    pred.time[i]=datetime.strptime(jointb.time[i], '%Y-%m-%d %H:%M')
    pred.state[i]=jointb.State[i]
    pred.low[i]=sorted(EEV)[int(sim_num/20)]
    pred.ave[i]=np.mean(EEV)
    pred.high[i]=sorted(EEV)[int(19*sim_num/20)]

# keep only the last value at a certain time. And remove NAs.
pred=pred.drop_duplicates(subset='time', keep='last').dropna(axis=0, how='all')
pred.index = np.arange(0,len(pred))

#%%
# read the USD/MXN data
# data found here http://www.histdata.com/download-free-forex-historical-data/?/metatrader/1-minute-bar-quotes/usdmxn/2016
# my_data = np.genfromtxt('DAT_MT_USDMXN_M1_2016.csv', delimiter=',')


with open('DAT_MT_USDMXN_M1_2016.csv',newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    fx=list(data)

fx = pd.DataFrame(fx)

#the sixth column is 0, drop it
fx = fx.drop(fx.columns[6], 1)

# average the minute values.
fx['mean'] = fx.ix[:,2:5].astype(float).mean(axis=1)

# extract time value to datetime format
fx['time'] = fx.ix[:,0]+fx.ix[:,1]
fx['time'] = [datetime.strptime(v, '%Y.%m.%d%H:%M') for v in fx['time']]

fx = fx.set_index(['time'])
fx = fx.loc[pred.time[0]:pred.time[len(pred)-1]]
fx = fx.drop(fx.columns[0:6],1)

#%%
#plotting
fig, ax1 = plt.subplots()
ax1.plot_date(pred.time, pred.low,'b--', label='95% confidence')
ax1.plot_date(pred.time, pred.ave,'r-', label='expected electoral votes')
ax1.plot_date(pred.time, pred.high,'b--', label='95% confidence')
plt.ylabel('Expected Votes')
pylab.legend(loc='lower right')

ax2 = ax1.twinx()
ax2.plot(fx['mean'],'g', label='Exchange Rate')

HMFmt = mdates.DateFormatter('%H:%M')
ax1.xaxis.set_major_formatter(HMFmt)
_ = plt.xticks(rotation=90)

plt.ylabel('USD/MXN')

pylab.legend(loc='upper right')
plt.show()



#%%

"""


#logistic regression model
logreg = linear_model.LogisticRegression(C=1e5)
h = .02

for i in range(2,len(jointb)-1):
    X=jointb['poll'][0:i].values.reshape(-1,1)
    Y=jointb['result'][0:i].values
    logreg.fit(X, Y)
    
    pred = logreg.predict(jointb['poll'].values[i:].reshape(-1,1))
    tot = np.append(Y,pred)
    
    EEV=tot.astype(float)*jointb['EV'].astype(float)
#    print(sum(EEV))
    
    pred2 = logreg.predict_proba(jointb.values[i:,1].reshape(-1,1))
    tot2 = np.append(Y,pred2[:,1])
    EEV2 = tot2.astype(float)*jointb['EV'].astype(float)
    print(jointb['time'][i], jointb['State'][i], sum(EEV2))
    
    
    error=np.subtract(logreg.predict(jointb.values[i:,1].reshape(-1,1)).astype(float), jointb.values[i:,2].astype(float))
#    print(np.mean(error))
    

#%%
#Assume we know the perent difference
#http://www.bbc.com/news/world/us_and_canada/states/dc

regr = linear_model.LinearRegression()

for i in range(2,len(jointb)-1):
    X=jointb['poll'][0:i].values.reshape(-1,1)
    Y=jointb['diff'][0:i].values
    regr.fit(X, Y)

    pred = regr.predict(jointb['poll'].values[i:].reshape(-1,1))
    pred= [1 if v > 0 else 0 for v in pred]
    
    call = jointb['result'][0:i].values
    tot = np.append(call,pred)
    
    EEV=tot.astype(float)*jointb['EV'].astype(float)
    print(jointb['time'][i],jointb['State'][i], sum(EEV))
    
#%%
#iris = datasets.load_iris()
#X = iris.data[:, :2]  # we only take the first two features.
#Y = iris.target
#
#h = .02  # step size in the mesh
#
#logreg = linear_model.LogisticRegression(C=1e5)
#
## we create an instance of Neighbours Classifier and fit the data.
#logreg.fit(X, Y)
#
## Plot the decision boundary. For that, we will assign a color to each
## point in the mesh [x_min, x_max]x[y_min, y_max].
#x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
#y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
#xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
#Z = logreg.predict(np.c_[xx.ravel(), yy.ravel()])
#
## Put the result into a color plot
#Z = Z.reshape(xx.shape)
#plt.figure(1, figsize=(4, 3))
#plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Paired)
#
## Plot also the training points
#plt.scatter(X[:, 0], X[:, 1], c=Y, edgecolors='k', cmap=plt.cm.Paired)
#plt.xlabel('Sepal length')
#plt.ylabel('Sepal width')
#
#plt.xlim(xx.min(), xx.max())
#plt.ylim(yy.min(), yy.max())
#plt.xticks(())
#plt.yticks(())
#
#plt.show()

"""