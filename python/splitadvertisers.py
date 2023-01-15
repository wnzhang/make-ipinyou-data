#!/usr/bin/python3
import sys
import os

if len(sys.argv) < 5:
    print('Usage: ipinyou.folder 25 train.log.txt test.log.txt')
    # python splitadvertisers.py ../ 25 ../all/train.log.txt ../all/test.log.txt
    exit(-1)

ifolder = sys.argv[1]
if not ifolder.endswith('/'):
    ifolder = ifolder + '/'

adidx = int(sys.argv[2])

for i in range(3, len(sys.argv)):
    fi = open(sys.argv[i], 'r')
    first = True
    advertiserFos = {}
    hearder = ""
    for line in fi:
        if first:
            first  = False
            header = line
            continue
        advertiser = line.split('\t')[adidx]
        if advertiser not in advertiserFos:
            if not os.path.exists(ifolder + advertiser):
                os.makedirs(ifolder + advertiser)
            fname = sys.argv[i][(sys.argv[i].rfind('/') + 1):]
            advertiserFos[advertiser] = open(ifolder + advertiser + '/' + fname, 'w')
            advertiserFos[advertiser].write(header)
        advertiserFos[advertiser].write(line)
    for advertiser in advertiserFos:
        advertiserFos[advertiser].close()
