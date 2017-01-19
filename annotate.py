#!/usr/bin/env python

import numpy as np
import os
import cv2
import argparse
import dicttoxml
import collections
from xml.dom.minidom import parseString

parser = argparse.ArgumentParser(description='Annotate APC data')
parser.add_argument('offset', type=int)
parser.add_argument('classname', type=str)

args = parser.parse_args()

drawing = False
ix,iy = -1,-1
bndbox = {}
classes = ['barkely_bones', 'bunny_book', 'cherokee_tshirt',
           'clorox_brush', 'cloud_bear', 'command_hooks',
           'crayola_24_ct', 'creativity_stems', 'dasani_bottle',
           'easter_sippy_cup', 'elmers_school_glue', 'expo_eraser',
           'fitness_dumbell', 'folgers_coffee', 'glucose_up_bottle',
           'jane_dvd', 'jumbo_pencil_cup', 'kleenex_towels',
           'kygen_puppies', 'laugh_joke_book', 'pencils',
           'platinum_bowl', 'rawlings_baseball', 'safety_plugs',
           'scotch_tape', 'staples_cards', 'viva',
           'white_lightbulb', 'woods_cord']

def mouse_draw(event,x,y,flags,param):
    global drawing,ix,iy,bndbox	

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            img_temp = img.copy()
            cv2.rectangle(img_temp,(ix,iy),(x,y),(0,255,0),1)
            cv2.imshow('image',img_temp)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),1)
        cv2.imshow('image',img)

	height, width, depth = img.shape

	if x >= width:
	    x = width
	if y >= height:
	    y = height
	if x <= 0:
	    x = 1
	if y <= 0:
	    y = 1
	x_min = min(ix, x)
	y_min = min(iy, y)
	x_max = max(ix, x)
	y_max = max(iy, y)
        
        bndbox = {'xmin':x_min, 'ymin': y_min, 'xmax': x_max, 'ymax':y_max}
		
		
if __name__ == '__main__':

    if args.offset < 1:
        print 'The argument offset must be a positive integer...'
        exit(-1)
    if args.classname not in classes:
        print args.classname + ' classname is invalid, please check the name and try again...'
        print classes
        exit(-1)

    input_dir = 'Input'
    images = os.listdir(input_dir)

    list_fname = 'ImageSets/Main/' + args.classname + '_train.txt'

    #Warn user if file already exists
    if os.path.isfile(list_fname):
        print list_fname + ' already exists...are you done with this object?'
	exit(-1)
    
    list_file = open(list_fname, 'w')

    count = 1

    while count < args.offset:
        number = str(count).zfill(6)
        list_file.write(number + '\t-1\n')
        count = count + 1
    print count

    num_files = len(images)

    for image in images:

        number = str(count).zfill(6)

        list_file.write(number + '\t1\n')

        input_file = os.path.join(input_dir, image)
        
        xml_file_name = 'Annotations/' + number + '.xml'
        img_file_name = 'JPEGImages/' + number + '.jpg'
        
        img = cv2.imread(input_file, cv2.IMREAD_COLOR)
        
        if os.path.isfile(img_file_name) or os.path.isfile(xml_file_name):
            print 'File already exists...aborting...'
            exit(-1)
        
        cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
        cv2.setMouseCallback('image', mouse_draw)
        cv2.imshow('image', img)
        
        height,width,depth = img.shape
        
        source = {'database':'The APC2017 Database','annotation':'Python OpenCV ISL_LAB','image':'APC_IITK'}
        owner = {'name':'ISL_IITK'}
        size = {'width':width,'height':height,'depth':depth}
        
        annotation = {'folder':'APC2017',
                      'filename':number + '.jpg',
                      'source':source,
                      'owner':owner,
                      'size':size, 
                      'segmented':0}
        
        key = cv2.waitKey(0)
        
        object_ = {'name':args.classname,
                   'pose':'Unspecified',
                   'truncated':0,
                   'difficult':0,
                   'bndbox':bndbox}

        annotation['object'] = object_

        xml = dicttoxml.dicttoxml(annotation,attr_type=False,custom_root='annotation')
        dom = parseString(xml)
        
        count = count + 1
	num_files = num_files - 1
        cv2.destroyAllWindows()

        
	img_new = cv2.imread(input_file, cv2.IMREAD_COLOR)
        cv2.imwrite(img_file_name, img_new)
	xml_file = open(xml_file_name,'w')
	xml_file.write(dom.toprettyxml())
        xml_file.close()
	print str(num_files) + ' files remaining : ' + image
        
	if key == 1048603:
            break
	

    print count
    print 'This is the offset you need to enter next time...'

    while count < 6065:
        number = str(count).zfill(6)
        list_file.write(number + '\t-1\n')
        count = count + 1

    list_file.close()
