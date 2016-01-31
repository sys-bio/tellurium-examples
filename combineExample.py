# This script shows how to export antimony and phrasedml strings to
# combine archive. The script creates an omex file called 'combineexport'
# to the same directory that this script is located.

import tellurium as te

antstr = '''
model myModel
  S1 -> S2; k1*S1
  S1 = 10; S2 = 0
  k1 = 1
end
'''

phrastr = '''
  model1 = model "myModel"
  sim1 = simulate uniform(0, 5, 100)
  task1 = run sim1 on model1
  plot "Figure 1" time vs S1, S2
'''

exp = te.experiment(antstr, phrastr)

# Export as combine archive
exp.exportAsCombine('./combineexport.omex') 