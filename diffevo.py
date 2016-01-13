
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

# Create the experimental data
m = r.simulate (fit.timeStart, fit.timeEnd, fit.numberOfPoints)
#%%
x_data = m[:,0]
y_data = m[:,2]
for i in range (0, len (y_data)):
    t = np.random.normal (0, .3)
    y_data[i] = y_data[i] + t

r.resetToOrigin()
z = r.simulate (fit.timeStart, fit.timeEnd, 100)
x_data_init = z[:,0]
y_data_init = z[:,2]
#%%
# Compute the simulated data at the current parameter values
def objectiveFunc(p):
    r.resetToOrigin()  
    k1, k2, k3 = p
    #for i in range(0, fit.nParameters):
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
    
    #guess = [5,5] # initial guess for params
    #y0 = [1,0,0] # inital conditions for ODEs
    bounds = [(-10., 10.), (-10., 10.), (-10., 10.)]
    result = differential_evolution(objectiveFunc, bounds)
    
    pop1.append (result.x[0])
    pop2.append (result.x[1])
    pop3.append (result.x[2])
    
#%%    
# Plot histograms showing the distribution of fitted parameters
    
#import seaborn as sb
#
#pal = sb.color_palette("hls", 3)
#
#sb.set_style("white")

binno = 30

fig = plt.figure(figsize=(15,10))
fig.set_dpi(1200)
ax = fig.add_subplot(111)
ax.tick_params(axis='x', pad=20)
ax.tick_params(axis='y', pad=20)
ax.tick_params('both', length=10, width=3, which='major')
ax.tick_params('both', length=10, width=3, which='minor')
ax.spines['top'].set_linewidth(3)
ax.spines['right'].set_linewidth(3)
ax.spines['left'].set_linewidth(3)
ax.spines['bottom'].set_linewidth(3)
plt.hist(pop1, bins=binno, normed=True, histtype='stepfilled', color='r', alpha=0.5)
plt.xticks(fontsize = 60)
plt.yticks(fontsize = 0)
plt.xlabel('$k_{1}$', fontsize = 60)
plt.ylabel('Frequency', fontsize = 60)
#fig.savefig(r'diffevofit_k1.eps', bbox_extra_artists=(), bbox_inches='tight', pad_inches=.5)
plt.show()

fig = plt.figure(figsize=(15,10))
fig.set_dpi(1200)
ax = fig.add_subplot(111)
ax.tick_params(axis='x', pad=20)
ax.tick_params('both', length=10, width=3, which='major')
ax.tick_params('both', length=10, width=3, which='minor')
ax.spines['top'].set_linewidth(3)
ax.spines['right'].set_linewidth(3)
ax.spines['left'].set_linewidth(3)
ax.spines['bottom'].set_linewidth(3)
plt.hist(pop2, bins=binno, normed=True, histtype='stepfilled', color='r', alpha=0.5)
plt.xticks(fontsize = 60)
plt.yticks(fontsize = 0)
plt.xlabel('$k_{2}$', fontsize = 60)
plt.ylabel('Frequency', fontsize = 60)
#fig.savefig(r'diffevofit_k2.eps', bbox_extra_artists=(), bbox_inches='tight', pad_inches=.5)
plt.show()

fig = plt.figure(figsize=(15,10))
fig.set_dpi(1200)
ax = fig.add_subplot(111)
ax.tick_params(axis='x', pad=20)
ax.tick_params('both', length=10, width=3, which='major')
ax.tick_params('both', length=10, width=3, which='minor')
ax.spines['top'].set_linewidth(3)
ax.spines['right'].set_linewidth(3)
ax.spines['left'].set_linewidth(3)
ax.spines['bottom'].set_linewidth(3)
plt.hist(pop3, bins=binno, normed=True, histtype='stepfilled', color='r', alpha=0.5)
plt.xticks(fontsize = 60)
plt.xticks(np.arange(0.49, 0.58, .02))
plt.yticks(fontsize = 0)
plt.xlabel('$k_{3}$', fontsize = 60)
plt.ylabel('Frequency', fontsize = 60)
#fig.savefig(r'diffevofit_k3.eps', bbox_extra_artists=(), bbox_inches='tight', pad_inches=.5)
plt.show()

#print "parameter values are ", p
cmap = matplotlib.cm.winter

fig = plt.figure(figsize=(15,10))
fig.set_dpi(1200)
ax = fig.add_subplot(111)
ax.tick_params(axis='x', pad=20)
ax.tick_params(axis='y', pad=20)
#frame.axes.get_yaxis().set_ticks([])
ax.tick_params('both', length=10, width=3, which='major')
ax.tick_params('both', length=10, width=3, which='minor')
ax.spines['top'].set_linewidth(3)
ax.spines['right'].set_linewidth(3)
ax.spines['left'].set_linewidth(3)
ax.spines['bottom'].set_linewidth(3)

for i in range (n):
    r.resetToOrigin()
    r.model[fittingClass.toFit[0]] = pop1[i]
    r.model[fittingClass.toFit[1]] = pop2[i]
    r.model[fittingClass.toFit[2]] = pop3[i]
    w = r.simulate (0, 10, 100)
    # Plot experimental data
    # Plot fitted model
    plt.plot (w[:,0], w[:,2], lw = 10, c='g', alpha=.1)
plt.plot (x_data, y_data, 'bo', markersize=15)    
plt.plot(x_data_init, y_data_init, lw=10,ls='--', c='r')
plt.yticks(fontsize = 60)
plt.xticks(fontsize = 60)
plt.yticks(np.arange(0, 6.1, 2.))
#plt.axis([0, 10, 0, .6])    
plt.xlabel('Time',{"fontsize":60})
plt.ylabel("S2 Concentration",{"fontsize":60})
#plt.legend(('data','actual','fit'),loc=0, fontsize=30)
#fig.savefig(r'diffevofit.eps', bbox_extra_artists=(), bbox_inches='tight', pad_inches=.5)
plt.show()