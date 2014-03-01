#!/usr/bin/python
# Author: Anders Ruberg

# This script is triggered when camera is connected with USB.
# My camera, Canon Powershot S110, doesn't support USB mass storage mode, only PTP mode.
# The camera is automatically mounted by gvfs. To access the files


import os


LOG_DEBUG = "debug"
LOG_INFO = "info"
import syslog

def log(string, type=LOG_INFO):
    syslog.syslog(string)


# Create lockfile to prevent HTPC to suspend
open('/home/anders/.cameracopy_suspendlock', 'a').close()
log("lock file created")

# Camera is mounted on ~/.gvfs
# Start sortphotos.py to move pictures
#for root, dirs, files in os.walk("~/", followlinks = True):
#    print "apa"
#    for name in files:
#        print name


os.remove('/home/anders/.cameracopy_suspendlock')
log("lock file removed")
