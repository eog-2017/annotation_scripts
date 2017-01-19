#!/usr/bin/env python

import os

count = 1

while count < 5242:
    number = str(count).zfill(6)
    if not os.path.isfile('Annotations/' + number + '.xml'):
        print 'Anno', count
    if not os.path.isfile('JPEGImages/' + number + '.jpg'):
        print 'JPEG', count

    count = count + 1    

