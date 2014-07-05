import sys, re, os, subprocess, string
import shutil 
import MFspells as spells

from random import sample, choice
from shutil import move
from sys import argv
from replacementvars import *
from foocoinvars import *

# osx (-osx), or unix (-unix) (makefile)?
sysflag = argv[1]
# search and replace
for search, replace in zip(searchvars, replacementvars):
    print ("\n\nSearching for: %s\nReplacing with: %s" %(search, replace))
    spells.multisearch(search, replace) 

# rename entire dir
print "Moving . . ."
shutil.move(Scname_lc, Rcname_lc)
if os.path.exists(Rcname_lc) == True:
    print "Renamed %s to %s" % (Scname_lc, Rcname_lc)

# rename qt.pro
print "Moving . . ."
profile_old = os.path.join(Rcname_lc, Scname_lc + "-qt.pro")
profile_new = os.path.join(Rcname_lc, Rcname_lc + "-qt.pro")
os.rename(profile_old, profile_new)
if os.path.exists(profile_new) == True:
    print "Renamed %s to %s" % (profile_old, profile_new)

# first compile
makepath = os.path.join(Rcname_lc, "src/")
makefile(sysflag)

# executing daemon to generate merkle hash in ~/.coin/coin.conf
spells.hardexecute("%s/src/%sd" % (Rcname_lc, Rcname_lc)) 
  
# search the tail of the log file for the merkle hash and set it to var
badGHash = "0000000000000000000000000000000000000000000000000000000000000000"
log = os.path.join("/root/." + Rcname_lc, "debug.log")
with open(log) as f:
    lines = f.readlines()
    for i in range(0, len(lines)):
        line = lines[i]
        if badGHash in line: # if genesis hash is string of 0s
            mhash = lines[i + 1] # grab merkle hash
            mhash = ''.join(mhash.split()) # make sure no whitespaces, tabs, or new lines get by
            break

# paste merkle hash in main.cpp
main = os.path.join(Rcname_lc, "src", "main.cpp")
stext = 'hashMerkleRoot == uint256("0x")'
rtext = 'hashMerkleRoot == uint256("0x' + mhash + '")' 
spells.infilereplace(main, stext, rtext)


# makefile 
makefile(sysflag)

# launching daemon to hash genesis block
spells.hardexecute("%s/src/%sd" % (Rcname_lc, Rcname_lc)) 


# search through debug.log and set genhash and nonce to vars
snonceline = "block.nNonce"
sghash = "block.GetHash"
with open(log) as f:
    lines = f.readlines()
    for i in range(0, len(lines)):
        line = lines[i]
        if snonceline in line: # if block nonce is found
            print "found block nonce!"
            nonceline = lines[i] # grab line that contains nonce
            nonce = nonceline[15:] # grab nonce from nonce line
            print "i grabbed the nonce!"
            nonce = ''.join(nonce.split()) # make sure no whitespaces get by
        if sghash in line: # if ghash is found 
            print "found genesis hash!"
            ghashline = lines[i] # grab the line that contains ghash
            ghash = ghashline[16:] # grab ghash from ghash line
            print "i grabbed the ghash!"
            ghash = ''.join(ghash.split()) # make sure no whitespaces get by
            break

# paste genhash and nonce into main.cpp and genhash into checkpoints.cpp
sghash = 'int256 hashGenesisBlock("0x")'
rghash = 'int256 hashGenesisBlock("0x' + ghash + '")' 
spells.infilereplace(main, sghash, rghash)

snonce = "block.nNonce   = 0;"
rnonce = "block.nNonce   = " + nonce + ";"
spells.infilereplace(main, snonce, rnonce)

stext = "(true && block.GetHash() != hashGenesisBlock)" 
rtext = "(false && block.GetHash() != hashGenesisBlock)"
spells.infilereplace(main, stext, rtext)

checkpoints = os.path.join(Rcname_lc, "src", "checkpoints.cpp")
stext = 'uint256("0x"))'
rtext = 'uint256("0x' + ghash + '"))'
spells.infilereplace(checkpoints, stext, rtext)
 
# makefile
makefile(sysflag)

# make conf files
rpcuser = Rcname_lc + "rpc"
# generate password
chars = string.letters + string.digits
length = 22
rpcpass = ''.join(choice(chars) for _ in xrange(length))
confpath = os.path.join("/root", "." + Rcname_lc, Rcname_lc + ".conf")
fo = open(confpath, "w+")
fo.write( "rpcuser=%s\nrpcpassword=%s\nlisten=1\nserver=1" % (rpcuser, rpcpass))
fo.close()


print "EXTRA DONE!"

# scp barcoin to derek
#spells.execute("scp -r %s root@107.170.242.134:~/Business/" % Rcname_lc)
#spells.execute("scp -r %s root@107.170.242.134:~/.%s/" % (confpath, Rcname_lc))



