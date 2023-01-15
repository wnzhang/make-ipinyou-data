#!/usr/bin/python3
import sys
from datetime import date

if len(sys.argv) < 3:
    print('Usage: schema clickfiles')
    exit(-1)

schema = [ s.strip() for s in open(sys.argv[1]).read().split() ]

tindex = schema.index('timestamp')
cindex = schema.index('creative')

bmap = {}
for fn in sys.argv[2:]:
    lcnt = 0
    for l in open(fn):
        arr = l.split('\t')
        bid = arr[0] +'-'+ arr[cindex]
        bmap[bid] = lcnt
# schema of ipinyou

fi = sys.stdin
fo = sys.stdout

fo.write( ('click\tweekday\thour\t'+'\t'.join(schema)) + '\n' )

for l in fi:
    arr = l.split('\t')
    bid = arr[0] +'-'+ arr[cindex]
    if bid in bmap:        
        fo.write('1')
    else:
        fo.write('0')
    ts = arr[tindex]
    d = date(int(ts[0:4]), int(ts[4:6]), int(ts[6:8]))
    fo.write('\t%d\t%s\t' % (int(d.strftime("%w")), arr[tindex][8:10]))
    fo.write( l )
