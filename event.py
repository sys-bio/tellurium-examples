

# Event example

import tellurium as te
import roadrunner

r = te.loada("""
        const S1, S4; 
        
        S1 -> S2; k1*S1;
        S2 -> S3; k2*S2;
        S3 -> S4; k3*S3;
        
        at time > 2: k2 = k2*5;
        at time > 8: k2 = k2/5;
        
        k1 = 0.45; k2 = 0.33; k3 = 0.87;
        S1 = 10; S2 = 0; S3 = 0; S4 = 0;
""")

#te.saveToFile ('c:\\IMAG\\eventDemo.xml', r.getSBML(level=2, version=4))

r.simulate (0, 20, 500, ['time', 'k2', 'S2', 'S3'])
r.plot()






