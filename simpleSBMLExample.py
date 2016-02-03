"""
An example script of using simpleSBML package to create SBML string.
simpleSBML creates valid SBML strings in a simple and fast manner.
"""
import simplesbml

m = simplesbml.sbmlModel()

# Add species to model
m.addSpecies("$X0", 1.0)
m.addSpecies("X1", 0.0)
m.addSpecies("X2", 0.0)
m.addSpecies("$X3", 0.0)

# Define parameters
m.addParameter("k1", 0.1)
m.addParameter("k2", 0.2)
m.addParameter("k3", 0.15)

# Define reactions
m.addReaction("[X0]", "[X1]", "k1*X0")
m.addReaction("[X1]", "[X2]", "k2*X1")
m.addReaction("[X2]", "[X3]", "k3*X2")

# Convert to SBML string
sbmlStr = m.toSBML()

# Print SBML
print(sbmlStr)
