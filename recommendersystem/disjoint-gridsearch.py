import numpy as np
from numpy.linalg import inv


a=0
r_imp=0
r_cli = 0
k=36
d=6
i=0



def set_articles(articles,param):
 
    global a, r_imp,r_cli
    a=param[0]
    r_imp = param[1]
    r_cli =param[2]
    #print param
    global A_a
    A_a = {x:np.identity(d) for x in articles}
    
    global inv_Aa
    inv_Aa = {x:inv(np.identity(d)) for x in articles}

    global b_a
    b_a = {x:np.zeros((d,1)) for x in articles}

    global theta_hat
    theta_hat = {x:np.dot(inv_Aa.get(x),b_a.get(x)) for x in articles}

    global art 
    art = articles
    return 0


def update(reward):
    if reward == -1:
	return
    elif reward == 0:
	reward =r_imp	
    else:
	reward = r_cli
    #print reward
    global A_0, b_0, A_a, z, x, B_a, b_a

    A_a[chosen] = A_a.get(chosen) + np.dot(x,x.T)

    b_a[chosen] = b_a.get(chosen) + reward*x

    inv_Aa[chosen] = inv(A_a.get(chosen))

    theta_hat[chosen] = np.dot(inv_Aa.get(chosen),b_a.get(chosen))
    return 0


def recommend(time, user_features, choices):
    global chosen, z, x
    best = (0,-np.inf)

    x = np.asarray(user_features).reshape(-1,1)
    #print x

    
#    theta_hats = np.matmul([inv_Aa[choice] for choice in choices],[b_a[choice] for choice in choices])
#    p =  theta_hats.transpose(0, 2, 1)*x_ta  + np.ndarray.flatten(np.asarray([a*np.sqrt(x_ta.T*inv_Aa[choice]*x_ta) for choice in choices]))
#      

    for choice in choices:
	#theta_hat = np.matmul(inv_Aa.get(choice),b_a.get(choice))
    	p_ta = np.dot(theta_hat.get(choice).T,x) + a*np.sqrt(np.dot(x.T,np.dot(inv_Aa.get(choice),x)))
	if p_ta>best[1]:
	    best = (choice, p_ta)


    #chosen = choices[np.argmax(p_ta)] 
    
    chosen = best[0]


    global i
    #i+=1
    #if i%1000==0:
    #    print i
    return chosen
