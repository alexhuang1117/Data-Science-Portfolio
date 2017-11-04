import numpy as np


learning_rate=100
batch_size=100
momentum=0.95
sample_times =1000

def transform(X):
    # Make sure this function works for both 1D and 2D NumPy arrays.
    return X


def mapper(key, value):
    # key: None
    # value: one line of input file
 #   if not 'w' in globals():
#        global w,t
    w=np.random.randn(400)
    t=1


    data = np.matrix([v.split(' ') for v in value])
    grad_old=0
    w_old=w
    w_diff=0
    for i in range(0, sample_times):
	ind = np.random.randint(len(data), size=batch_size)
        y = data[ind,0].astype(float)
        x = data[ind,1:].astype(float)

        result=np.multiply(np.transpose(np.matmul(x,np.transpose(w))), y)
        result = (result<1).astype(int)


        x_time_y = np.multiply(x,y)
	grad = np.multiply(x_time_y,result).mean(axis=0)
#	grad_aj = momentum*(grad-grad_old)
        w =np.squeeze(np.array(w + learning_rate/(t**0.5)*grad + momentum*w_diff))
#	grad_old = grad_aj
	
	w_diff = w-w_old
	w_old=w
	
        if i>len(value)/batch_size/2:
	    
	    print sum(result.astype(float))/batch_size
	    yield 0, w
        t += 1
	
    	  # This is how you yield a key, value pair


def reducer(key, values):
    # key: key from mapper used to aggregate
    # values: list of all value for that key
    # Note that we do *not* output a (key, value) pair here.
    print np.squeeze(np.asarray(values))

    yield np.squeeze(np.asarray(values)).mean(axis=0)
