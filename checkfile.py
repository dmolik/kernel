#!/usr/bin/python3.2

import urllib
import bz2
import os
import multiprocessing

def ckpatcher():
  urllib.urlretrieve ("http://ck.kolivas.org/patches/3.0/3.3/3.3-ck1/patch-3.3-ck1.bz2", "patch-3.3-ck1.bz2")
  bz = bz2.BZ2File('patch-3.3-ck1.bz2', 'r')
  with open('patch-3.3-ck1', 'w') as f:
    data = bz.read()
    f.write(data)
  bz.close()

checkck = os.path.isfile('patch-3.3-ck1')

if not checkck:
  print 'Patching kernel with ck1'
  ckpatcher()
else:
  print 'All set'
  print 'herp'
print multiprocessing.cpu_count()

