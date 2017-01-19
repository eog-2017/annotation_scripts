#!/usr/bin/env python
import os
import shutil

count = 3113

files_ = os.listdir('raw/ashish/jane_dvd')

for file_ in files_:
    if count == 3133:
        shutil.copy('raw/ashish/jane_dvd/'+file_, 'Input')
      
    count = count + 1

'''rename = 2154

while count > 1926:
    ren = str(rename).zfill(6)
    name = str(count).zfill(6)

    shutil.copyfile('corrupt/'+name+'.jpg', 'JPEGImages/'+ren+'.jpg')

    xml = open('corrupt/'+name+'.xml', 'r')
    xml_new = open('Annotations/'+ren+'.xml', 'w')

    for line in xml:
        if 'filename' in line:
            replace = line.replace(name, ren)
        else:
            replace = line

        xml_new.write(replace)

    xml_new.close()
    xml.close()
    count = count - 1
    rename = rename - 1'''

