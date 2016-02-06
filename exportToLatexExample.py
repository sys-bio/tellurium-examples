"""
This script shows how to export plots produced from roadrunner to Latex.
The script creates three text files: 'Model_code.txt', 'Model_data1.txt',
'Model_data2.txt'. 'Model_code.txt' contains Latex script that can be
compiled to get a pdf file using pgfplots package. Other two files contain
data points to plot the figure for species S1 and S2. The script will create
files to the same directory that this script is located.
"""
import tellurium as te

r = te.loada('''
    $Xo -> S1; vo;
    S1 -> S2; k1*S1 - k2*S2;
    S2 -> $X1; k3*S2;
    
    vo = 1
    k1 = 2; k2 = 0; k3 = 3;
''')

result = r.simulate(0, 6, 100)

p = te.LatexExport(r,
    color=['blue', 'green'],
    legend=['S1', 'S2'],
    xlabel='Time',
    ylabel='Concentration',
    exportComplete=True,
    saveto='./'
)

p.saveToFile(result)
