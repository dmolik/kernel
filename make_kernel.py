#!/usr/bin/python3.2

import subprocess
import urllib
import bz2
def ckpatcher
  urllib.urlretrieve ("http://ck.kolivas.org/patches/3.0/3.3/3.3-ck1/patch-3.3-ck1.bz2", "/usr/src/patch-3.3-ck1.bz2")
  bz = bz2.BZ2File('/usr/src/patch-3.3-ck1.bz2', 'r')
  with open('/usr/src/linux/patch-3.3-ck1', 'w') as f:
    data = bz.read()
    f.write(data)
  bz.close()

checkck = os.path.isfile('/usr/src/usr/src/patch-3.3-ck1.bz2')

if 
retcode = subprocess.Popen(["ls","-l1a"], stdout=subprocess.PIPE).communicate()[0]
print retcode

cd /usr/src
patchck=`ls -1 patch*ck*` || ( wget http://ck.kolivas.org/patches/3.0/3.3/3.3-ck1/patch-3.3-ck1.bz2 && bzip2 -d patch-3.3-ck1.bz2 )
cd linux
if [[ -z `ls -1 $patchck` ]] ; then 
	cp ../$patchck .
	patch -p1 < $patchck
fi
cp ../.config .
vers=`pwd -P`
vers=${vers##'/'*'/'}
vers=${vers##'linux-'}
make oldconfig
cp .config ../
cores=`cat /proc/cpuinfo | sed '/cpu\ cores[\t\:\ ]*/!d' | sed '1q' | sed 's/cpu\ cores\t\:\ //'`
cpus=`cat /proc/cpuinfo | sed '/physical\ id[\t\:\ ]*/!d' | sed '$!d' | sed 's/physical\ id\t\:\ //'`
let "cpus=cpus+1"
let "total=cores*cpus"
make -j$total
make modules_install
make headers_install 
emerge aufs3 nvidia-drivers openafs-kernel
make -j$total
make modules_install
make headers_install 
mount /boot
cp arch/x86/boot/bzImage /boot/kernel-$vers-ck
cd /usr/src
boot-update
umount /boot

