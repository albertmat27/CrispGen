#!/usr/bin/python2.7

import fileinput, glob, string, sys, os
from os.path import join

stext = sys.argv[1]
rtext = sys.argv[2]
path = join(sys.argv[3], "*")

# print "stext: %s\nrtext %s\npath %s" %(stext, rtext, path)

files = glob.glob(path)

for line in fileinput.input(files,inplace=1):
    lineno = 0
    lineno = string.find(line, stext)
    if lineno >0:
        line = line.replace(stext, rtext)

    sys.stdout.write(line)
