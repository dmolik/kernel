#!/usr/bin/python3.2

import subprocess
import urllib
import bz2

urllib.urlretrieve ("http://ck.kolivas.org/patches/3.0/3.3/3.3-ck1/patch-3.3-ck1.bz2", "patch-3.3-ck1.bz2")
bz = bz2.BZ2File('patch-3.3-ck1.bz2', 'r')
with open('patch-3.3-ck1', 'w') as f:
  data = bz.read()
  f.write(data)
bz.close()
  
