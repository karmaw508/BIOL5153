##!/usr/bin/bash/python
 
#used the same sequence used in chapter 2 and named it genomic_dna.txt 
dna_file = open("genomic_dna.txt")
my_dna = dna_file.read()

# extracted the different bits of DNA sequence
exon1 = my_dna[0:62]
intron = my_dna[62:90]
exon2 = my_dna[90:10000]

# opened the two output files
coding_file = open("coding_dna.txt", "w")
noncoding_file = open("noncoding_dna.txt", "w")

# write the sequences to the output files
coding_file.write(exon1 + exon2)
noncoding_file.write(intron)