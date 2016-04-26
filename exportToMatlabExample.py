"""
This script shows how to export models into executable MATLAB .m file.
The script creates a file called 'testmodel.m' to the same directory that
this script is located.
"""
import tellurium as te
import os.path

r = te.loada('''
model testmodel
    $Xo -> S1; vo;
    S1 -> S2; k1*S1 - k2*S2;
    S2 -> $X1; k3*S2;
    
    vo = 1
    k1 = 2; k2 = 0; k3 = 3; 
end
''')

# Export model as a Matlab function
r.exportToMatlab(os.path.join('.', 'testmodel.m'))
