#!/usr/bin/python3
import sys
import os

if len(sys.argv) < 2:
    print('Usage: input')
    exit(-1)


oses = ["windows", "ios", "mac", "android", "linux"]
browsers = ["chrome", "sogou", "maxthon", "safari", "firefox", "theworld", "opera", "ie"]

fi = open(sys.argv[1], 'r')
outname = sys.argv[1] + ".fmua"
fo = open(outname, 'w')

first = True
for l in fi:
    if first:
        fo.write(l)
        first = False
        continue
    s = l.split('\t')
    ua = s[7].lower()
    operation = "other"
    browser = "other"
    for o in oses:
        if o in ua:
            operation = o
            break
    for b in browsers:
        if b in ua:
            browser = b
            break
    fmua = operation + "_" + browser
    output = s[0]
    for i in range(1, len(s)):
        if i == 7:
            output = output + '\t' + fmua
        else:
            if len(s[i]) == 0 or s[i] == '\n':
                s[i] = "null" + s[i]
            output = output + '\t' + s[i]
    fo.write(output)
fo.close()

os.rename(outname, sys.argv[1])
