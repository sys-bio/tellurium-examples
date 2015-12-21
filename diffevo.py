
# Fitting using differential evolution, also showing 
# distribution of fitted parameters as a histogram

import pylab as plt
import numpy as np
import tellurium as te
import matplotlib
import roadrunner
from scipy.optimize import differential_evolution
import time

r = te.loada("""
   S1 -> S2; k1*S1;
   S2 -> S3; k2*S2;
   
   S1 = 1; S2 = 0; S3 = 0; 
   k1 = 0.15; k2 = 0.45; 
""")

class fittingClass:
         toFit = ['k1', 'k2']
         nParameters = len (toFit)
         timeStart = 0
         timeEnd = 10
         numberOfPoints = 11

# Randomize random number generator
np.random.seed (int (time.time()))
fit = fittingClass()

# Create the experimental data
m = r.simulate (fit.timeStart, fit.timeEnd, fit.numberOfPoints)
#%%
x_data = m[:,0]
y_data = m[:,2]
for i in range (0, len (y_data)):
    t = np.random.normal (0, 0.05)
    y_data[i] = y_data[i] + t
#%%
# Compute the simulated data at the current parameter values
def objectiveFunc(p):
    r.reset()  
    k1, k2 = p
    #for i in range(0, fit.nParameters):
    r.model[fit.toFit[0]] = k1
    r.model[fit.toFit[1]] = k2
    
    s = r.simulate (fit.timeStart, fit.timeEnd, fit.numberOfPoints)
    
    a1 = y_data - s[:,2]
    return np.sum (a1*a1)


# Run optimizer n times and store fitted parameters in a list
pop1 = []
pop2 = []
n = 100
for i in range (n):   
    #guess = [5,5] # initial guess for params
    #y0 = [1,0,0] # inital conditions for ODEs

    bounds = [(-5, 5), (-5, 5)]
    result = differential_evolution(objectiveFunc, bounds)
    print(result.x)
    pop1.append (result.x[0])
    pop2.append (result.x[1])
    #print result.x, result.fun

# Plot histograms showing the distribution of fitted parameters
binno = 30
plt.hist(pop1, bins=binno, normed=True, histtype='stepfilled', color='r', alpha=0.5)
plt.show()

plt.hist(pop2, bins=binno, normed=True, histtype='stepfilled', color='r', alpha=0.5)
plt.show()

#print "parameter values are ", p
cmap = matplotlib.cm.winter

for i in range (n):
    r.reset()
    r.model[fittingClass.toFit[0]] = pop1[i]
    r.model[fittingClass.toFit[1]] = pop2[i]
    t = r.simulate (0, 10, 100)
    # Plot experimental data
    plt.plot (x_data, y_data, '.r')
    # Plot fitted model
    plt.plot (t[:,0], t[:,2], lw = 3, c='b', alpha=.1)
    
plt.xlabel('Time',{"fontsize":16})
plt.ylabel("Concentration, S2",{"fontsize":16})
plt.legend(('data','fit'),loc=0)
plt.show()