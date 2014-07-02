import sys, re, os, calendar, time, subprocess
import shutil 
import MFspells as spells

from shutil import move
from sys import argv
from replacementvars import *
from foocoinvars import *

# osx (-osx), or unix (-unix) (makefile)?
sysflag = argv[1]
#script, search = argv      

# what variables will be searched for and replaced
searchvars = (Scname_lc, Scname_uc , Scname_mc, Sname_qt, Scabbrev, Srpc, Sp2p, Stestnet, 
              Sseedsite, Sseedip, Sblockreward, Sblockfreq, Sdifficultyfreq, Smaxcoins, 
              Sblockstoday, Saddressletter, Sepoch, Sepoch_hreadable)   

# replacements in replacements.py
current_epoch = calendar.timegm(time.gmtime())
Repoch =  "block.nTime    = %s" %(current_epoch)

replacementvars = (Rcname_lc, Rcname_uc , Rcname_mc, Rname_qt, Rcabbrev, Rrpc, Rp2p, Rtestnet, 
                   Rseedsite, Rseedip, Rblockreward, Rblockfreq, Rdifficultyfreq, Rmaxcoins, 
                   Rblockstoday, Raddressletter, Repoch, Repoch_hreadable)

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

makepath = os.path.join(Rcname_lc, "src/")
print """Makefile path is %s\n
         Executing Makefile... """ % (makepath)

if (sysflag == "-osx"):
    spells.execute("make -C %s -f %s USE_UPNP=-" % (makepath, "makefile.osx"))

elif (sysflag == "-unix"):
    spells.execute("make -C %s -f %s USE_UPNP=-" % (makepath, "makefile.unix"))

else:
    sys.exit("You gave: [%s]\nAcceptable flags are [-unix] or [-osx], sir." % sysflag)
 
print "DONE!"   
    



