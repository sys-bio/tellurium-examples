"""
This script constructs a gene cassette.
"""

from sbol import *

setHomespace("http://sys-bio.org")
doc = Document()

gene = ComponentDefinition("BB0001")
promoter = ComponentDefinition("R0010")
CDS = ComponentDefinition("B0032")
RBS = ComponentDefinition("E0040")
terminator = ComponentDefinition("B0012")

promoter.roles.set(SO_PROMOTER)
CDS.roles.set(SO_CDS)
RBS.roles.set(SO_RBS)
terminator.roles.set(SO_TERMINATOR)

doc.addComponentDefinition(gene)
doc.addComponentDefinition(promoter)
doc.addComponentDefinition(CDS)
doc.addComponentDefinition(RBS)
doc.addComponentDefinition(terminator)

gene.assemble([ promoter, RBS, CDS, terminator ])

first = gene.getFirstComponent()
print(first.identity.get())
last = gene.getLastComponent()
print(last.identity.get())

promoter_seq = Sequence("R0010", "ggctgca")
RBS_seq = Sequence("B0032", "aattatataaa")
CDS_seq = Sequence("E0040", "atgtaa")
terminator_seq = Sequence("B0012", "attcga")
gene_seq = Sequence("BB0001")

doc.addSequence(promoter_seq)
doc.addSequence(CDS_seq)
doc.addSequence(RBS_seq)
doc.addSequence(terminator_seq)
doc.addSequence(gene_seq)

promoter.sequence.set(promoter_seq.identity.get())
CDS.sequence.set(CDS_seq.identity.get())
RBS.sequence.set(RBS_seq.identity.get())
terminator.sequence.set(terminator_seq.identity.get())
gene.sequence.set(gene_seq.identity.get())

gene_seq.assemble()
print(gene_seq.elements.get())

doc.write("gene_cassette.xml")
