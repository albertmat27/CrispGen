import re, os

from sys import argv

# passing variables
#script, search, replacement = argv
script, search = argv
#replace = "yomomma"
#replacement = "caterpillar"

# defining walking search (it is case sensitive)
def multisearch(search, replacement):
# walk the directory tree, search, and replace
    for dname, dirs, files in os.walk("./SRtest"):
        for fname in files:
            fpath = os.path.join(dname, fname)
            with open(fpath) as f:
                s = f.read()
            s = s.replace(search, replacement)
            with open(fpath, "w") as f:
                f.write(s)

def multisearchTEST(search):
    for dname, dirs, files in os.walk("./foocoin-master"):
        for fname in files:
            fpath = os.path.join(dname, fname)
            text = open(fpath, "r")
            for line in text:
                if re.match("(.*)%s(.*)"%search, line):
                    print ("I found this:\n'%s'" %(line))
            

# what is being searched
Scname_lc = "foocoin"
Scname_uc = "FOOCOIN"
Scname_mc = "FooCoin"
Scabbrev = "FOO"
Srpc = "55883"
Sp2p = "55884"
Stestnet = "45884"
Sseedsite = "some website name"
Sseedip = "somewebsite.org or ip x.x.x.x"
Sblockreward = "nSubsidy = 1"
Sblockfreq = "nTargetSpacing = 120" # seconds
Sdifficultyfreq = "nTargetTimespan = 1" # days
Smaxcoins = "MAX_MONEY = 10000"
Sblockstoday = "dPriority > COIN * 720"
Saddressletter = "PUBKEY_ADDRESS = 38" # set to 11 for C
Sepoch =  "block.nTime    = 1300000000"
Sepoch_hreadable = "Traditionally one puts something timely here coinciding with the epoch"

searchvars = (Scname_lc, Scname_uc , Scname_mc, Scabbrev, Srpc, Sp2p, Stestnet, Sseedsite, 
              Sseedip, Sblockreward, Sblockfreq, Sdifficultyfreq, Smaxcoins, Sblockstoday, 
              Saddressletter, Sepoch, Sepoch_hreadable)   

for item in searchvars:
    print ("Searching for %s sir . . ." %(item))
    multisearchTEST(item) 

#multisearchTEST(search)
