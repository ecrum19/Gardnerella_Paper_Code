The code contributions of author Elias Crum to the publication DOI: 10.1128/mSphere.00154-21 <br/>
This repo contains code used to obtain Gardnerella genomes, pull core genes from Gardnerella sequences, and visualize an ANI analysis of the CORE genes.<br/><br/>



Workflow:

Compare.py - data preprocesssing file used to ensure all Gardnerella sequence files intended for use in the study were present on local machine

Anvi'o pangenome analysis and single copy core genome determination (done through linux Anvi'o tool in a Conda virtual environment)

COG_Genes.py - script used to determine the indentity of the core genes detemined by anvi'o in each Gardnerella sequence

Unrooted phylogenetic tree of core genome was produced using linux tool iqtree - "iqtree -s Core_genome_file.fa -m MFP -bb 1000 -alrt 1000 -nt AUTO"

ANI analysis was performed using "fastANI" local tool; BASH file was used to compare all gardnerella sequences to all gardnerella sequences

ANI_plot.py - Matplotlib library was used to produce heat map of similar and non-similar Gardnerella sequences using fastANI output data
