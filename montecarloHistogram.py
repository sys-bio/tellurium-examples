"""
Monteo Carlo simulation of a stright chain pathway
Samples parameter values while keeping Keq constant
Plots the distribtution of control coefficients
"""

import tellurium as te
import random
import matplotlib.pyplot as plt
import numpy as np
import time

r = te.loada("""
   J1: $Xo -> S1;  (k1*Xo - k1/Keq1*S1);
     S1 -> S2;  k2*S1 - k2/Keq2*S2;
     S2 -> S3;  k3*S2 - k3/Keq3*S3;
     S3 -> $X1; k4*S3 - k4/Keq4*X1;
     
     k1 = 0.1; k2 = 0.1;
     k3 = 0.1; k4 = 0.1;
     
     Keq1 = 4;
     Keq2 = 3;
     Keq3 = 2;
     Keq4 = 1;
     Xo = 5;
     X1 = 0.1;
     ki = 1
     n = 6
""")

# Randomize
np.random.seed(int(time.time()))

m = r.simulate(0, 10, 100)
C1 = r.getCC('J1', 'k1')
C2 = r.getCC('J1', 'k2')
C3 = r.getCC('J1', 'k3')
C4 = r.getCC('J1', 'k4')

print C1, C2, C3, C4
sum = C1 + C2 + C3 + C4
print sum

# Initialize
aC1 = 0; aC2 = 0; aC3 = 0; aC4 = 0;
aC1a = []; aC2a = []; aC3a = []; aC4a = [];
n = 1000  # Number of repetition
upperLimitK = 10.

# Run simulation n times and calculate control coefficients each run
for i in range(0, n):
    r.setValue('k1', random.uniform(0, upperLimitK))
    r.setValue('k2', random.uniform(0, upperLimitK))
    r.setValue('k3', random.uniform(0, upperLimitK))
    r.setValue('k4', random.uniform(0, upperLimitK))
    r.simulate()    
    r.steadyState()
    C1 = r.getCC('J1', 'k1')
    C2 = r.getCC('J1', 'k2')
    C3 = r.getCC('J1', 'k3')
    C4 = r.getCC('J1', 'k4')
    aC1 = aC1 + C1
    aC2 = aC2 + C2
    aC3 = aC3 + C3
    aC4 = aC4 + C4
    aC1a.append(C1)
    aC2a.append(C2)
    aC3a.append(C3)
    aC4a.append(C4)

print aC1/n, aC2/n, aC3/n, aC4/n 

# Plot
bins = 100
fig = plt.figure()

ax = fig.add_subplot(111)
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')
ax.tick_params(axis='x', pad=20)
ax.tick_params(axis='y', pad=0)


ax1 = fig.add_subplot(2,2,1)
plt.yticks(fontsize=0)
plt.xticks(fontsize=20)
plt.axis([0,1,0,4])
plt.xticks(np.arange(0, 1.1, .5))
ax1.annotate("k1", xy=(0.97, 3.5), xytext=(0.875, 3.4), fontsize=20)
plt.hist(aC1a, bins=bins, histtype='stepfilled', normed=True, color='b', label='C1')

ax2 = fig.add_subplot(2,2,2)
plt.yticks(fontsize=0)
plt.xticks(fontsize=20)
plt.axis([0,1,0,5])
plt.xticks(np.arange(0, 1.1, .5))
ax2.annotate("k2", xy=(0.97, 4.5), xytext=(0.875, 4.25), fontsize=20)
plt.hist(aC2a, bins=bins, histtype='stepfilled', normed=True, color='g', label='C2')

ax3 = fig.add_subplot(2,2,3)
plt.yticks(fontsize=0)
plt.xticks(fontsize=20)
plt.axis([0,.6,0,15])
plt.xticks(np.arange(0, .61, .3))
ax3.annotate("k3", xy=(0.54, 14.5), xytext=(0.525, 12.8), fontsize=20)
plt.hist(aC3a, bins=bins, histtype='stepfilled', normed=True, color='r', label='C3')

ax4 = fig.add_subplot(2,2,4)
plt.yticks(fontsize=0)
plt.xticks(fontsize=20)
plt.axis([0,.6,0,25])
plt.xticks(np.arange(0, .61, .3))
ax4.annotate("k4", xy=(0.54, 24.5), xytext=(0.525, 21.2), fontsize=20)
plt.hist(aC4a, bins=bins, histtype='stepfilled', normed=True, color='purple', label='C4')

plt.tight_layout(w_pad=1)
ax.set_xlabel("Control Coefficients", fontsize=25)
ax.set_ylabel("Normalized Frequency", fontsize=25)
plt.show()
