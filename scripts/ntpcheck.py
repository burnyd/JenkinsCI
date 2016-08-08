#!/usr/bin/python

#Simple test to check to see if the ntp server is working properly.

import pyeapi
import json
import time
import jinja2

veos02 = pyeapi.connect_to('veos02')
ntpstatus = veos02.enable('show ntp status')
ntpstatusvalues = ntpstatus[0]['result'].values()

for i in ntpstatusvalues:
    if i.find("unsynchronised") != -1:
        print "It didnt work"
        raise Exception("time did not sync")
    else 
        print "It did work"
