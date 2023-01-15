#!/usr/bin/python3
import sys
import operator

if len(sys.argv) < 5:
    print('Usage: train.log.txt test.log.txt train.lr.txt test.lr.txt featindex.txt')
    exit(-1)

oses = ["windows", "ios", "mac", "android", "linux"]
browsers = ["chrome", "sogou", "maxthon", "safari", "firefox", "theworld", "opera", "ie"]

f1s = ["weekday", "hour", "IP", "region", "city", "adexchange", "domain", "slotid", "slotwidth", "slotheight", "slotvisibility", "slotformat", "creative", "advertiser"]

f1sp = ["useragent", "slotprice"]

f2s = ["weekday,region"]

def featTrans(name, content):
    content = content.lower()
    if name == "useragent":
        operation = "other"
        for o in oses:
            if o in content:
                operation = o
                break
        browser = "other"
        for b in browsers:
            if b in content:
                browser = b
                break
        return operation + "_" + browser
    if name == "slotprice":
        price = int(content)
        if price > 100:
            return "101+"
        elif price > 50:
            return "51-100"
        elif price > 10:
            return "11-50"
        elif price > 0:
            return "1-10"
        else:
            return "0"

def getTags(content):
    if content == '\n' or len(content) == 0:
        return ["null"]
    return content.strip().split(',')

# initialize
namecol = {}
featindex = {}
maxindex = 0
fi = open(sys.argv[1], 'r')
first = True

featindex['truncate'] = maxindex
maxindex += 1

for line in fi:
    s = line.split('\t')
    if first:
        first = False
        for i in range(0, len(s)):
            namecol[s[i].strip()] = i
            if i > 0:
                featindex[str(i) + ':other'] = maxindex
                maxindex += 1
        continue
    for f in f1s:
        col = namecol[f]
        content = s[col]
        feat = str(col) + ':' + content
        if feat not in featindex:
            featindex[feat] = maxindex
            maxindex += 1
    for f in f1sp:
        col = namecol[f]
        content = featTrans(f, s[col])
        feat = str(col) + ':' + content
        if feat not in featindex:
            featindex[feat] = maxindex
            maxindex += 1
    col = namecol["usertag"]
    tags = getTags(s[col])
    for tag in tags:
        feat = str(col) + ':' + tag
        if feat not in featindex:
            featindex[feat] = maxindex
            maxindex += 1

print('feature size: ' + str(maxindex))
featvalue = sorted(featindex.items(), key=operator.itemgetter(1))
fo = open(sys.argv[5], 'w')
for fv in featvalue:
    fo.write(fv[0] + '\t' + str(fv[1]) + '\n')
fo.close()

# indexing train
print('indexing ' + sys.argv[1])
fi = open(sys.argv[1], 'r')
fo = open(sys.argv[3], 'w')

first = True
for line in fi:
    if first:
        first = False
        continue
    s = line.split('\t')
    fo.write(s[0] + ' ' + s[23]) # click + winning price
    index = featindex['truncate']
    fo.write(' ' + str(index) + ":1")
    for f in f1s: # every direct first order feature
        col = namecol[f]
        content = s[col]
        feat = str(col) + ':' + content
        if feat not in featindex:
            feat = str(col) + ':other'
        index = featindex[feat]
        fo.write(' ' + str(index) + ":1")
    for f in f1sp:
        col = namecol[f]
        content = featTrans(f, s[col])
        feat = str(col) + ':' + content
        if feat not in featindex:
            feat = str(col) + ':other'
        index = featindex[feat]
        fo.write(' ' + str(index) + ":1")
    col = namecol["usertag"]
    tags = getTags(s[col])
    for tag in tags:
        feat = str(col) + ':' + tag
        if feat not in featindex:
            feat = str(col) + ':other'
        index = featindex[feat]
        fo.write(' ' + str(index) + ":1")
    fo.write('\n')
fo.close()

# indexing test
print('indexing ' + sys.argv[2])
fi = open(sys.argv[2], 'r')
fo = open(sys.argv[4], 'w')

first = True
for line in fi:
    if first:
        first = False
        continue
    s = line.split('\t')
    fo.write(s[0] + ' ' + s[23]) # click + winning price
    index = featindex['truncate']
    fo.write(' ' + str(index) + ":1")
    for f in f1s: # every direct first order feature
        col = namecol[f]
        if col >= len(s):
            print('col: ' + str(col))
            print(line)
        content = s[col]
        feat = str(col) + ':' + content
        if feat not in featindex:
            feat = str(col) + ':other'
        index = featindex[feat]
        fo.write(' ' + str(index) + ":1")
    for f in f1sp:
        col = namecol[f]
        content = featTrans(f, s[col])
        feat = str(col) + ':' + content
        if feat not in featindex:
            feat = str(col) + ':other'
        index = featindex[feat]
        fo.write(' ' + str(index) + ":1")
    col = namecol["usertag"]
    tags = getTags(s[col])
    for tag in tags:
        feat = str(col) + ':' + tag
        if feat not in featindex:
            feat = str(col) + ':other'
        index = featindex[feat]
        fo.write(' ' + str(index) + ":1")
    fo.write('\n')
fo.close()
