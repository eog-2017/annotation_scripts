#!/usr/bin/env python

import os
import random

f = open('train.txt')

lines = []

for line in f:
    lines.append(line.replace('\n', ''))


random.shuffle(lines)

out_train = open('Main/trainval.txt', 'w')

for line in lines:
    out_train.write(line+'\n')

in_filen = os.listdir('Original/')

in_files = {}
out_files = {}

for in_file in in_filen:
    curr_file = open('Original/' + in_file, 'r')
    in_files[in_file] = []
    for line in curr_file:
	in_files[in_file].append(line)
    out_files[in_file] = []
    curr_file.close()
   
for in_file in in_filen:
    for line in lines:
    	index = int(line) - 1
    	out_files[in_file].append(in_files[in_file][index])

#print lines[1]
#print out_files['pencils_train.txt'][1]

for in_file in in_filen:
    out_file = open('Main/' + in_file, 'w')
    curr_list = out_files[in_file]
    for line in curr_list:
	out_file.write(line)
    out_file.close()
