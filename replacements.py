# replacements.py
import calendar, time

#what are the replacements
Rcname_lc = "tomahawkcoin" # lowercase
Rcname_uc = "TOMAHAWK" # CAPS
Rcname_mc = "TomahawkCoin" # Mixed
Rname_qt = "Tomahawkcoin" # qt
Rcabbrev = "TMK" # CAPS 
Rrpc = "55765"
Rp2p = "55766"
Rtestnet = "55767"
Rseedsite = "crispcoin.net"
Rseedip = "107.170.242.134"
Rblockreward = "nSubsidy = 1000000"
Rblockfreq = "nTargetSpacing = 30" # seconds
Rdifficultyfreq = "nTargetTimespan = 1" # days
Rmaxcoins = "MAX_MONEY = 10000000"
Rblockstoday = "dPriority > COIN * 10"
Raddressletter = "PUBKEY_ADDRESS = 11" # set to 11 for C
Repoch_hreadable = "Today"

# replacements
current_epoch = calendar.timegm(time.gmtime())
Repoch =  "block.nTime    = %s" %(current_epoch)

replacementvars = (Rcname_lc, Rcname_uc , Rcname_mc, Rname_qt, Rcabbrev, Rrpc, Rp2p, Rtestnet, 
                   Rseedsite, Rseedip, Rblockreward, Rblockfreq, Rdifficultyfreq, Rmaxcoins, 
                   Rblockstoday, Raddressletter, Repoch, Repoch_hreadable)

