import os
import numpy as np

lista = np.linspace(0.1,0.7,6)
reward1 = range(1,50,5)
reward2 = np.linspace(-1,1,10)
reward3 = np.linspace(-1,1,4)
for a in lista:
    for r1 in reward1:
	for r2 in reward2:
	    for r3 in reward3:
		os.system("python2 runner.py data/webscope-logs.txt data/webscope-articles.txt disjoint.py",a,r1,r2,r3)
