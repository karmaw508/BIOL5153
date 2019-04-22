#! /usr/bin/python


from __future__ import division 
import argparse

parser = argparse.ArgumentParser(description = "")

parser.add_argument( "-gf", "--gff", help="the name of the gff file", default="watermelon.gff")
parser.add_argument( "-fa", "--fasta", help="the name of the fasta file", default="watermelon.fsa")

args = parser.parse_args()

# Reading gff file 
gff_file = args.gff
gff = open(gff_file, "r") 
gff_output = open("gff_output.file", "w")

for line in gff:
  fields = line.split("\t")
  start = int(fields[3]) 
  stop = int(fields[4])
  
  gff_substring = (fields[3], fields[4]) 
 
  gff_output.write(str(start) + "\t" + str(stop) + "\n") 


# Reading fasta file 
fasta = args.fasta
fasta_file = open(fasta, "r")
fasta_output = open("gff_output.file")

substring = open("substring.txt", "w")

for lines in fasta_output:
  positions = lines.split('\t')
  start = int(positions[0])
  stop = int(positions[1])
  substring_sequence = fasta[start:stop]
  print(substring_sequence)
  substring_file.write(substring_seq)
    
# Calculating the GC content 

my_substring = open("substring.txt").read()
length = len(my_substring)
g_count = my_substring.count('G')
c_count = my_substring.count('C')

print("length: " + str(length))
print("g count: " + str(g_count))
print("C count: " + str(c_count))

gc_content = (g_count + c_count) / length 

print("gc content: " + str(gc_content))

# Reverse Complement 
