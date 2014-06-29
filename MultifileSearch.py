import re, os, calendar, time

from sys import argv
from replacements import *

# passing variables
#script, search, replacement = argv
#script, search = argv
#replace = "yomomma"
#replacement = "caterpillar"

# defining walking search (it is case sensitive)
def multisearch(search, replacement):
# walk the directory tree, search, and replace
    count = 0
    for dname, dirs, files in os.walk("./foocoin"):
        for fname in files:
            fpath = os.path.join(dname, fname)
            with open(fpath) as f:
                s = f.read()
            if search in s:
                s = s.replace(search, replacement)
                count +=1
            with open(fpath, "w") as f:
                f.write(s)
    print "%s instances of {%s} were replaced with {%s}." %(count, search, replacement)
    
def multisearchTEST(search):
    for dname, dirs, files in os.walk("./foocoin"):
        for fname in files:
            fpath = os.path.join(dname, fname)
            text = open(fpath, "r")
            for line in text:
                if re.match("(.*)%s(.*)"%search, line):
                    print "I found this:\n'%s'" %(line)
            

# what is being searched
Scname_lc = "foocoin" # lowercase
Scname_uc = "FOOCOIN" # CAPS
Scname_mc = "FooCoin" # Mixed
Sname_qt = "Foocoin" # qt
Scabbrev = "FOO" # CAPS
Srpc = "55883"
Sp2p = "55884"
Stestnet = "45884"
Sseedsite = "andarazoroflove"
Sseedip = Rseedsite + ".org"
Sblockreward = "nSubsidy = 1"
Sblockfreq = "nTargetSpacing = 120" # seconds
Sdifficultyfreq = "nTargetTimespan = 1" # days
Smaxcoins = "MAX_MONEY = 10000"
Sblockstoday = "dPriority > COIN * 576"
Saddressletter = "PUBKEY_ADDRESS = 38" # set to 11 for C
Sepoch =  "block.nTime    = 1300000000"
Sepoch_hreadable = "Traditionally one puts something timely here coinciding with the epoch"

searchvars = (Scname_lc, Scname_uc , Scname_mc, Sname_qt, Scabbrev, Srpc, Sp2p, Stestnet, 
              Sseedsite, Sseedip, Sblockreward, Sblockfreq, Sdifficultyfreq, Smaxcoins, 
              Sblockstoday, Saddressletter, Sepoch, Sepoch_hreadable)   

# for loop used to test
#for item in searchvars:
#    print ("Searching for %s sir . . ." %(item))
#    multisearchTEST(item) 

# replacements in replacements.py
current_epoch = calendar.timegm(time.gmtime())
Repoch =  "block.nTime    = %s" %(current_epoch)

replacementvars = (Rcname_lc, Rcname_uc , Rcname_mc, Rname_qt, Rcabbrev, Rrpc, Rp2p, Rtestnet, 
                   Rseedsite, Rseedip, Rblockreward, Rblockfreq, Rdifficultyfreq, Rmaxcoins, 
                   Rblockstoday, Raddressletter, Repoch, Repoch_hreadable)

# for loop used to search and replace
for search, replace in zip(searchvars, replacementvars):
    print ("Searching for \n%s\nreplacing with\n%s\n\n" %(search, replace))
    multisearch(search, replace) 

print "DONE!"


