# This script shows how to export models into executable MATLAB .m file.
# The script creates a file called 'model.m' to the same directory that 
# this script is located. 

import tellurium as te

r = te.loada('''
    $Xo -> S1; vo;
    S1 -> S2; k1*S1 - k2*S2;
    S2 -> $X1; k3*S2;
    
    vo = 1
    k1 = 2; k2 = 0; k3 = 3;
''')

# Export model as a Matlab function
r.exportToMatlab(r'.\model.m')