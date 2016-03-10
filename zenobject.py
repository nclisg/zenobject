#!/usr/bin/env python 
"""
Generates Manufacuter Hardwware objects for use in Zenpacks
Format csv as follows: 

s5320-32P-EI-DC,.1.3.6.1.4.1.2011.2.23.305
s5720-52X-EI-AC,.1.3.6.1.4.1.2011.2.23.306
s5320-52X-EI-AC,.1.3.6.1.4.1.2011.2.23.307

"""

import sys

if len(sys.argv) < 2:
    print "Need to provide a csv file!" 
    sys.exit(0)
    

f = open(sys.argv[1])

for line in f:
    data = line.split(',')
    model = data[0]
    oid = data[1].rstrip('\n')

    print "<object id='" + model +"' module='Products.ZenModel.HardwareClass' class='HardwareClass'>"
    print '<property type="string" id="name" mode="w" >'
    print model
    print '</property>\n<property type="lines" id="productKeys" mode="w" >'
    print "['" + oid + "']"
    print '</property><property type="boolean" id="isOS" mode="w" >\nFalse\n</property>\n</object>'

