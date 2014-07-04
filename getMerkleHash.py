import os, sys

from foocoinvars import *
from replacementvars import *

# read debug.log line by line
# if line is 0 * 64
#	then read next line
#   else sys.exit(complain)

badGHash = "0000000000000000000000000000000000000000000000000000000000000000"

log = os.path.join("/root/." + Rcname_lc + "/backups", "debug.log")
with open(log) as f:
    lines = f.readlines()
    for i in range(0, len(lines)):
        line = lines[i]
        if badGHash in line: # if genesis hash is string of 0s
            mhash = lines[i + 1] # grab merkle hash
            mhash.strip() # make sure no whitespaces get by
            break
print mhash

"""
log = os.path.join("/root/." + Rcname_lc + "/backups", "debug.log")
with open(log) as f:
    while True:
        nextline = f.readline()
        print nextline
        if "0000000000000000000000000000000000000000000000000000000000000000" in nextline:
            mhash = f.readline(nextline + 1)
        if nextline == '':
            break
print mhash
   """ 
