import subprocess, sys, shutil, errno, os
from subprocess import Popen

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

def execute(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    # Poll Process for new output until finished
    while True:
        nextline= process.stdout.readline()
        if nextline == '' and process.poll() != None:
            break
        sys.stdout.write(nextline)
        sys.stdout.flush()
        
    output = process.communicate()[0]
    exitCode = process.returncode

    if (exitCode == 0):
        return output
    else: raise
        #raise ProcessException(command, exitCode, output)
        
#execute("bash echotest.sh")

# copy anything
def copy(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc:
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise

