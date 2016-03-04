"""
This script performs bifucation analysis on embryonic stem cell model
"""
import platform

if 'darwin' in platform.system().lower():
    from rrplugins import *
else:
    from teplugins import *
import matplotlib.pyplot as plt

sbmlModel ="BIOMD0000000203.xml"                              
auto = Plugin("tel_auto2000")              
    
# Setup properties
auto.setProperty("SBML", readAllText(sbmlModel))

# Bifurcation specific properties
auto.setProperty("ScanDirection", "Positive")    
auto.setProperty("PrincipalContinuationParameter", "A")
auto.setProperty("PCPLowerBound", 10)
auto.setProperty("PCPUpperBound", 150)
    
# Set maximum numberof points
auto.setProperty("NMX", 5000)  
       
# execute the plugin
auto.execute()
         
# plot Bifurcation diagram
pts     = auto.BifurcationPoints
lbls    = auto.BifurcationLabels
biData  = auto.BifurcationData    
biData.plotBifurcationDiagram(pts, lbls) 
