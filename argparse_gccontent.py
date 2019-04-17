#! /usr/bin/python 

from __future__ import division
import math 
import argparse

parser = argparse.ArgumentParser(description='Calculate the gc_content of substring')
parser.add_argument('g_count', type=int, help='G content')
parser.add_argument('c_count', type=int, help='C content')
args = parser.parse_args()

def area_rectangle(g_count, c_count): 
	my_subsring = open("substring.txt").read()
	length = len(my_substring)
	g_count = my_string.count('G')
	c_count = my_string.count('C')
	gc_content = (g_count + c_count) / length 
	return gc_content

if __name__== '__main__': 
	print gc_content of substring(args.g_count, args.c_count) 
