#!/usr/bin/python3.2

import urllib
import bz2
import os
import multiprocessing
import shutil
import subprocess
import platform

def compileKernel():
   os.chdir('/usr/src/linux')
   cores = multiprocessing.cpu_count()
   # Compile the kernel
   subprocess.call(['make', '-j'+str(cores)])
   subprocess.call(['make', 'modules_install'])
   subprocess.call(['make', 'headers_install'])
   
def checkProcessor():
   if platform.processor().lower().find('intel') != -1: 
      subprocess.call(['emerge', '-q', 'microcode_ctl', 'microcode-data' ])
      subprocess.call(['rc-update', 'add', 'microcode_ctl', 'default'])
   else:
      print "TODO: Add kernel config for amd processors"
   
def ckPatcher():
   urllib.urlretrieve ("http://ck.kolivas.org/patches/3.0/3.3/3.3-ck1/patch-3.3-ck1.bz2", "/usr/src/patch-3.3-ck1.bz2")
   bz = bz2.BZ2File('/usr/src/patch-3.3-ck1.bz2', 'r')
   with open('/usr/src/linux/patch-3.3-ck1', 'w') as f:
      data = bz.read()
      f.write(data)
   bz.close()
   os.chdir('/usr/src/linux')
   subprocess.call(['patch', '-p1', '<', 'patch-3.3-ck1'])

checkck = os.path.isfile('/usr/src/linux/patch-3.3-ck1')
if not checkck:
  ckPatcher() 

os.chdir('/usr/src/linux')

shutil.copy2('/usr/src/.config', '/usr/src/linux')
subprocess.call(['make', 'oldconfig'])
shutil.copy2('/usr/src/linux/.config', '/usr/src/')

cores = multiprocessing.cpu_count()

subprocess.call(['make', '-j'+str(cores)])

compileKernel()
# emerge packages that depend on the kernel
subprocess.call(['emerge', '-q', 'aufs3', 'nvidia-drivers', 'openafs-kernel', 'btrfs-progs' ])
checkProcessor()
compileKernel()

subprocess.call(['mount', '/boot'])

rentval = subprocess.Popen(["pwd","-P"], stdout=subprocess.PIPE).communicate()[0]
version = rentval.strip("/usr/src/linux")
version = version.strip('\r\n')
version = '/boot/kernel'+version+'-ck'
shutil.copy2('/usr/src/linux/arch/x86/boot/bzImage', version)

subprocess.call(['boot-update'])

subprocess.call(['umount', '/boot'])


