# CrisGen README by Albert Mata
# July 2 2014

Flags:
[-unix]
uses makefile.unix to make

[-osx]
uses makefile.osx to make 

Examples:
python coingen.py -unix

python coingen.py -osx

CrispGen has dependencies. Make sure the following sources exist in the same directory:
replacementvars.py (contains settings to be used for new coin)
MFspells.py (contains functions)
foocoin (contains foocoin sourcecode)
foocoinvars.py (contains foocoin variables to be replaced)

Given those dependencies, CrispGen walks the directory tree searching for the variables in foocoinvars.py, and replaces them with variables in replacementvars.py. It renames the coin home directory, and remaining files with the foocoin name. Then it executes the unix or osx makefile.


