# vars file
from replacementvars import Rseedsite

# what are the settings of foocoin that will be replaced
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

# what variables will be searched for and replaced
searchvars = (Scname_lc, Scname_uc , Scname_mc, Sname_qt, Scabbrev, Srpc, Sp2p, Stestnet, 
              Sseedsite, Sseedip, Sblockreward, Sblockfreq, Sdifficultyfreq, Smaxcoins, 
              Sblockstoday, Saddressletter, Sepoch, Sepoch_hreadable)   

