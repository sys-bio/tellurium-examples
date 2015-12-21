
# Monteo Carlo simulation of a stright chain pathway
# Samples parameter values while keeping Keq constant
# Plots the distribtution of control coefficients

import tellurium as te
import roadrunner
import random
import pylab as pl
import winsound

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

m = r.simulate (0, 10, 100);
C1 = r.getCC ('J1', 'k1')
C2 = r.getCC ('J1', 'k2')
C3 = r.getCC ('J1', 'k3')
C4 = r.getCC ('J1', 'k4')

print C1, C2, C3, C4
sum = C1 + C2 + C3 + C4;
print sum

aC1 = 0; aC2 = 0; aC3 = 0; aC4 = 0;
aC1a = []; aC2a = []; aC3a = []; aC4a = [];
n = 5000
upperLimitK = 50
for i in range (0,n):
    r.setValue ('k1', random.uniform(0, upperLimitK))
    r.setValue ('k2', random.uniform(0, upperLimitK))
    r.setValue ('k3', random.uniform(0, upperLimitK))
    r.setValue ('k4', random.uniform(0, upperLimitK))
    r.simulate()    
    r.steadyState()
    C1 = r.getCC ('J1', 'k1')
    C2 = r.getCC ('J1', 'k2')
    C3 = r.getCC ('J1', 'k3')
    C4 = r.getCC ('J1', 'k4')
    aC1 = aC1 + C1
    aC2 = aC2 + C2
    aC3 = aC3 + C3
    aC4 = aC4 + C4
    aC1a.append (C1)
    aC2a.append (C2)
    aC3a.append (C3)
    aC4a.append (C4)

print aC1/n, aC2/n, aC3/n, aC4/n 

bins = 100

pl.hist(aC1a, bins=bins, histtype='stepfilled', normed=True, color='r', alpha=0.5, label='C1')
pl.hist(aC2a, bins=bins, histtype='stepfilled', normed=True, color='b', alpha=0.5, label='C2')
pl.hist(aC3a, bins=bins, histtype='stepfilled', normed=True, color='g', alpha=0.5, label='C3')
pl.hist(aC4a, bins=bins, histtype='stepfilled', normed=True, color='y', alpha=0.5, label='C4')

    
