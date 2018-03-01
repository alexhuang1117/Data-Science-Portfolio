import numpy as np
from numpy.linalg import inv

a=0.6
k=36
d=6
i=0

def set_articles(articles):
 
    global A_0, b_0, inv_A0
    A_0 = np.asmatrix(np.identity(k))
    b_0 = np.asmatrix(np.zeros((k,1)))
    inv_A0 = inv(A_0)

    global A_a
    A_a = {x:np.asmatrix(np.identity(d)) for x in articles}
    global inv_Aa
    inv_Aa = {x:inv(np.asmatrix(np.identity(d))) for x in articles}
    global B_a
    B_a = {x:np.asmatrix(np.zeros((d,k))) for x in articles}
    global b_a
    b_a = {x:np.asmatrix(np.zeros((d,1))) for x in articles}
    
    global art 
    art = articles
    return 0


def update(reward):
    if reward == -1:
	reward = -0.1
    elif reward == 0:
	reward =-2		
    else:
	reward = 20


    #print reward
    global A_0, b_0, A_a, z, x, B_a, b_a
    
    A_0 = A_0+ B_a.get(chosen).T*inv_Aa.get(chosen)*B_a.get(chosen)
    b_0 = b_0 + B_a.get(chosen).T*inv_Aa.get(chosen)*b_a.get(chosen)
    A_a[chosen] = A_a.get(chosen) + x*x.T
    B_a[chosen] = B_a.get(chosen) + x*z.T
    b_a[chosen] = b_a.get(chosen) + reward*x
    inv_Aa[chosen] = inv(A_a.get(chosen))
    A_0 = A_0+ z*z.T - B_a.get(chosen).T*inv_Aa.get(chosen)*B_a.get(chosen)
    b_0 = b_0 + reward*z - B_a.get(chosen).T*inv_Aa.get(chosen)*b_a.get(chosen)
    inv_A_0 = inv(A_0)
    

    return 0


def recommend(time, user_features, choices):
    
    best = (-np.inf,-np.inf)
    x_ta = np.asmatrix(user_features).reshape((d,1))

    beta_hat = inv_A0*b_0
    for choice in choices:

	z_ta = np.outer(np.asarray(art.get(choice)).T,np.asarray(user_features)).reshape((k, 1))

	theta_hat = inv_Aa.get(choice)*(b_a.get(choice)-B_a.get(choice)*beta_hat)
	#print theta_hat.shape
	s_ta = z_ta.T*inv_A0*z_ta  - 2*z_ta.T*inv_A0*B_a.get(choice).T*inv_Aa.get(choice)*x_ta + \
		x_ta.T*inv_Aa.get(choice)*x_ta + x_ta.T*inv_Aa.get(choice)*B_a.get(choice)*inv_A0*B_a.get(choice).T*inv_Aa.get(choice)*x_ta
	p_ta = z_ta.T*beta_hat + x_ta.T*theta_hat + a*np.sqrt(s_ta)
	#print p_ta
	if p_ta>best[1]:
	    best = (choice, p_ta)
    global chosen, z, x
    chosen = best[0]
    	
    z = np.outer(np.asarray(art.get(chosen)).T,np.asarray(user_features)).reshape((k, 1))
    x = x_ta
    global i
    i+=1
    if i%1000==0:
        print i
    return best[0]
