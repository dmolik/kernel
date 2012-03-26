#!/usr/bin/python3.2

import platform

#import cpuinfo
print "platform.processor(): " + platform.processor()
print "platform.machine(): " + platform.machine()
print "platform.node(): " + platform.node()
print "platform.version(): " + platform.version()
print  platform.linux_distribution()

if platform.processor().lower().find('intel') != -1: 
   print "intel derp"
else:
   print "amd herp"

if platform.processor().lower().find('amd') != -1:
   print "amd derp"
else:
   print "intel herp"
   
#print cpuinfo.cpu.info[0]['model name']

