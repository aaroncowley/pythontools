#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

subprocess.call('clear',shell=True)

remoteHost = raw_input("enter remote host: ")
remoteIP = socket.gethostbyname(remoteHost)
t1 = datetime.now()
print "starting scan at", t1
print "scanning remote host", remoteIP

try:
    for port in range(1,1025):
        hostSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = hostSock.connect_ex((remoteIP,port))
        if result == 0:
            print "port{}:  OPEN".format(port)
        hostSock.close()

except KeyboardInterrupt:
    print "^C pressed"
    sys.exit()

except socket.gaierror:
    print 'Hostname could not be resolved'
    sys.exit()

except socket.error:
    print "Couldn't connect to server"
    sys.exit()

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
t2 = datetime.now()
total =  t2 - t1

# Printing the information to screen
print 'Scan wasted this much time: ', total

