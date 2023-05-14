
from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr
from collections import namedtuple
import os
# TODO Add your imports here 
import csv


log = core.getLogger()
policyFile = "%s/pox/pox/misc/firewall-policies.csv" % os.environ[ 'HOME' ]

#TODO Add your global variables here 
blocked_lst = []
firstline = True #use this to skip the first line in the csv file

with open(policyFile) as csvfile:
    readFile = csv.reader(csvfile, delimeter=',')
    #next(read) #delete if everything runs
    for row in readFile:
        if firstline:
            firstline = False
            continue
        print(row[1]) # delete after running
        blocked_lst.append(row[1])

    # Vary the number of blocked hosts
    # blocked_lst = blocked_lst[:-2] #1, 2, 3

class Firewall (EventMixin):

    def __init__ (self):
        self.listenTo(core.openflow)
        log.debug("Enabling Firewall Module")

    def _handle_ConnectionUp (self, event):
        #TODO Add your logic here
        for i in blocked_lst:
            block = of.ofp_match()
            block.dl_src = EthAddr(i)
            flow_mod = of.ofp_flow_mod()
            flow_mod.match = block
            event.connection.send(flow_mod)

        log.debug("Firewall rules installed on %s", dpidToStr(event.dpid))

def launch ():
    #    Starting the Firewall module
    
    core.registerNew(Firewall)
