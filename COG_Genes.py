import os
from subprocess import call

COG = "//Users/eliascrum/Desktop/COG/"
GG = "//Users/eliascrum/Desktop/GG4ANI/"
COG_list = []
GG_list = []

def list_file_dirs(folder):
    for fname in os.listdir(folder):
        if folder == COG:
            COG_list.append(os.path.abspath(fname))
        else:
            GG_list.append(os.path.abspath(fname))


def Genes_v_Genomes(GenomeL, GeneL):
    for gene in GeneL:
        for genome in GenomeL:
            command = 'makeblastdb -in %s -title myDB -out myDB -dbtype nucl'% (genome)
            os.system(command)
            command = 'blastn -db %s -query %s -max_target_seqs 1 -outfmt "10 qseqid sseqid sseq" -out %s.csv' % \
                      ("myDB", gene, gene + " " + genome)
            subprocess.call('cd /Users/eliascrum/Desktop/ncbi-blast-2.10.0+')
            os.system(command)

#test = call("vim", "cd d /Users/eliascrum/Desktop/ncbi-blast-2.10.0+")

list_file_dirs(COG)
list_file_dirs(GG)

##Genes_v_Genomes(GG_list, COG_list)

## /Users/eliascrum/Desktop/2020 - Spring/PutontiLab/GarnerellaProject/.DS_Store