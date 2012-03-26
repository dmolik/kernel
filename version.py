#!/usr/bin/python3.2

import re
import os 
import subprocess

os.chdir('/usr/src/linux')

retcode = subprocess.Popen(["pwd","-P"], stdout=subprocess.PIPE).communicate()[0]
rentval = retcode.strip("/usr/src/linux-")
print rentval
