#!/usr/bin/python3.2

import subprocess
import sys
import multiprocessing

# some code here
cores = multiprocessing.cpu_count()
#pid = subprocess.Popen([sys.executable, "longtask.py"]) 

a = "-j"+str(cores)

print a
