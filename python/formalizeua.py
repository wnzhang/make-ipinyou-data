#!/usr/bin/python
import sys
import os
from user_agents import parse

if len(sys.argv) < 2:
    print 'Usage: input'
    exit(-1)

fi = open(sys.argv[1], 'r')
outname = sys.argv[1] + ".fmua"
fo = open(outname, 'w')

first = True
for l in fi:
    if first:
	s = l.split('\t')
	output = s[0]
	for i in range(1,len(s)):
	    if i == 7:
		output = output + '\t' + '\t'.join(["device", "device_family", "os", "browser"])
	    else:
		output = output + '\t' + s[i]
        fo.write(output)
        first = False
    s = l.split('\t')
    ua = parse(s[7])
    if ua.is_mobile:
	device = "m"
    elif ua.is_tablet:
	device = "t"
    elif ua.is_pc:
	device = "c"
    else:
	device = "o"
    device_family = ua.device.family
    os_family = ua.os.family
    browser = ua.browser.family
    output = s[0]
    for i in range(1, len(s)):
        if i == 7:
            output = output + '\t' + '\t'.join([device, device_family,os_family,browser])
        else:
            if len(s[i]) == 0 or s[i] == '\n':
                s[i] = "null" + s[i]
            output = output + '\t' + s[i]
    fo.write(output)
fo.close()

os.rename(outname, sys.argv[1])
