"""
This script shows how to export run parameter scan and plot the output
as a surface plot.
"""
import tellurium as te

r = te.loada('''
    J1: $Xo -> x; 0.1 + k1*x^4/(k2+x^4);
    x -> $w; k3*x;

    k1 = 0.9;
    k2 = 0.3;
    k3 = 0.7;
    x = 0;
''')

p = te.ParameterScan(r,
    startTime = 0,
    endTime = 15,
    numberOfPoints = 50,
    polyNumber = 10,
    endValue = 1.8,
    alpha = 0.8,
    value = "x",
    selection = "x",
    color = ['#0F0F3D', '#141452', '#1A1A66', '#1F1F7A', '#24248F', '#2929A3',
               '#2E2EB8', '#3333CC', '#4747D1', '#5C5CD6']
)
# plot
p.plotPolyArray()
