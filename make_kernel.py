#!/usr/bin/python3.2

import subprocess
import urllib

import os
import tarfile
import zipfile

def extract_file(path, to_directory='.'):
    if path.endswith('.zip'):
        opener, mode = zipfile.ZipFile, 'r'
    elif path.endswith('.tar.gz') or path.endswith('.tgz'):
        opener, mode = tarfile.open, 'r:gz'
    elif path.endswith('.tar.bz2') or path.endswith('.tbz'):
        opener, mode = tarfile.open, 'r:bz2'
    else: 
        raise ValueError, "Could not extract `%s` as no appropriate extractor is found" % path
    
    cwd = os.getcwd()
    os.chdir(to_directory)
    
    try:
        file = opener(path, mode)
        try: file.extractall()
        finally: file.close()
    finally:
        os.chdir(cwd)

urllib.urlretrieve ("http://ck.kolivas.org/patches/3.0/3.3/3.3-ck1/patch-3.3-ck1.bz2", "/usr/src/patch-3.3-ck1.bz2")
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

