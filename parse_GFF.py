#! /usr/bin/python

import argparse

parser = argparse.ArgumentParser(description = "")

parser.add_argument( "-gf", "--gff", help="the name of the gff file", default="watermelon.gff")
parser.add_argument( "-fa", "--fasta", help="the name of the fasta file", default="watermelon.fsa")

args = parser.parse_args()

gff_file = args.gff
gff = open(gff_file, "r") 
gff_output = open("gff_output.file", "w")

for line in gff:
  fields = line.split("\t")
  start = int(fields[3]) 
  stop = int(fields[4])
 # print(str(start) + "\t" + str(stop))
  
  gff_substring = (fields[3], fields[4]) 
 
  gff_output.write(str(start) + "\t" + str(stop) + "\n") 



fasta = args.fasta
fasta_file = open(fasta, "r")
fasta_output = open("gff_output.file")

   				#fasta = open(fasta_file, "r") 
				#fasta_file = open(args.fasta).read()
				#fasta_output = open("gff_output.text")

substring = open("substring.txt", "w")

for lines in fasta_output:
  positions = lines.split('\t')
  start = int(positions[0])
  stop = int(positions[1])
  substring_sequence = fasta[start:stop]
  print(substring_sequence)



