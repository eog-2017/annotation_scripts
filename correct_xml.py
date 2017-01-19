#!/usr/bin/env python

import xmltodict
import dicttoxml
import os
from xml.dom.minidom import parseString

import shutil

list_files = os.listdir('Annotations/')

area = []

for file_ in list_files:
    with open('Annotations/'+file_, 'r') as fd:
        doc = xmltodict.parse(fd.read())
        xmax = int(doc['annotation']['object']['bndbox']['xmax'])
        xmin = int(doc['annotation']['object']['bndbox']['xmin'])
        ymax = int(doc['annotation']['object']['bndbox']['ymax'])
        ymin = int(doc['annotation']['object']['bndbox']['ymin'])
	if xmax <= xmin:
            print file_
            print 'error'
        if ymax <= ymin:
            print file_
            print 'error' 
        
        area.append((xmax-xmin)*(ymax-ymin))

print min(area)

'''	x_max = max(xmax, xmin)
	x_min = min(xmax, xmin)
	y_max = max(ymax, ymin)
	y_min = min(ymax, ymin)

        print x_max, y_max, x_min, y_min

        if x_max >= 640:
            x_max = 639
        if x_min < 0:
            x_min = 0
        if y_max >= 640:
            y_max = 639
        if y_min < 0:
            y_min = 0

        doc['annotation']['object']['bndbox']['xmax'] = x_max
        doc['annotation']['object']['bndbox']['xmin'] = x_min
        doc['annotation']['object']['bndbox']['ymax'] = y_max
        doc['annotation']['object']['bndbox']['ymin'] = y_min

        xml = dicttoxml.dicttoxml(doc, attr_type=False, root=False)
        dom = parseString(xml)
        
        with open('Annotations/' + file_, 'w') as fdd:
            fdd.write(dom.toprettyxml())'''
