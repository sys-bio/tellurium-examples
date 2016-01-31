# This script performs fitting using differential evolution and plots
# time course of synthetic, expected, and estimated data.

import pylab as plt
import numpy as np
import tellurium as te
from scipy.optimize import differential_evolution
import time

r = te.loada("""
   S1 -> S2; k1*S1 - k2*S2;
   S2 -> S3; k3*S2;
   
   S1 = 10; S2 = 1; S3 = 0;
   k1 = 0.67; k2 = 0.23; k3 = 0.55;
""")

class fittingClass:
         toFit = ['k1', 'k2', 'k3']
         nParameters = len (toFit)
         timeStart = 0
         timeEnd = 10
         numberOfPoints = 11

# Randomize random number generator
np.random.seed (int (time.time()))
fit = fittingClass()

# Create experimental data
m = r.simulate (fit.timeStart, fit.timeEnd, fit.numberOfPoints)
x_data = m[:,0]
y_data = m[:,2]
for i in range (0, len (y_data)):
    t = np.random.normal (0, .3)
    y_data[i] = y_data[i] + t

r.resetToOrigin()
z = r.simulate (fit.timeStart, fit.timeEnd, 100)
x_data_init = z[:,0]
y_data_init = z[:,2]

# Compute the simulated data and calculate the value of objective function
def objectiveFunc(p):
    r.resetToOrigin()  
    k1, k2, k3 = p
    r.model[fit.toFit[0]] = k1
    r.model[fit.toFit[1]] = k2
    r.model[fit.toFit[2]] = k3
    
    s = r.simulate (fit.timeStart, fit.timeEnd, fit.numberOfPoints)
    
    a1 = y_data - s[:,2]
    return np.sum (a1*a1)

# Run optimizer n times and store fitted parameters in a list
pop1 = []
pop2 = []
pop3 = []
n = 100
for i in range (n):   
    bounds = [(-10., 10.), (-10., 10.), (-10., 10.)] # Range of parameters
    result = differential_evolution(objectiveFunc, bounds)
    pop1.append (result.x[0])
    pop2.append (result.x[1])
    pop3.append (result.x[2])
    
# Plot
fig = plt.figure()
for i in range (n):
    r.resetToOrigin()
    r.model[fittingClass.toFit[0]] = pop1[i]
    r.model[fittingClass.toFit[1]] = pop2[i]
    r.model[fittingClass.toFit[2]] = pop3[i]
    w = r.simulate (0, 10, 100)
    estim, = plt.plot (w[:,0], w[:,2], lw = 5, c='g')

syn, = plt.plot (x_data, y_data, marker = 'o', c = 'b', markersize = 10, linestyle = "None")
expe, = plt.plot(x_data_init, y_data_init, lw = 5, ls='--', c='r')

plt.yticks(fontsize = 20)
plt.xticks(fontsize = 20)
plt.yticks(np.arange(0, 6.1, 2.))
plt.legend([syn, expe, estim], ["Synthetic", "Expected", "Estimated"], fontsize=20)
ax = plt.gca()
legend = ax.get_legend()
legend.legendHandles[0].set_color('g')
legend.legendHandles[1].set_color('b')
legend.legendHandles[2].set_color('r')
plt.xlabel('Time',{"fontsize":25})
plt.ylabel("$S_{2}$ Concentration",{"fontsize":25})
plt.show()
