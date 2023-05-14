#!/usr/bin/python

# EEE4121F-B Lab 2
# SDN

# Implementing a Layer-2 Firewall using POX and Mininet


from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.clean import cleanup

def treeTopo():
    cleanup()
    net = Mininet( controller=RemoteController )

    # Create the controller object and connect it to the network
    net.addController('c0')

    # Create 8 host objects and add them to the network
    for i in range(8):
        net.addHost('h%s' % (i+1), ip='10.0.0.%s' % (i+1), mac='00:00:00:00:00:0%s' % (i+1))

    # Create 7 switch objects and add them to the network
    for i in range(7):
        net.addSwitch('s%s' % (i+1))

    # Finally, create the links as described in the figure
    # Switch links to root
    net.addLink('s1','s2')
    net.addLink('s1','s5')

    # Layer 1 switch links
    net.addLink('s2','s3')
    net.addLink('s2','s4')

    # Layer 2 switch links
    net.addLink('s5','s6')
    net.addLink('s5','s7')

    # Host links
    net.addLink('h1', 's3')
    net.addLink('h2', 's3')
    net.addLink('h3', 's4')
    net.addLink('h4', 's4')
    net.addLink('h5', 's6')
    net.addLink('h6', 's6')
    net.addLink('h7', 's7')
    net.addLink('h8', 's7')

    # Start the mininet network, start the CLI interface, and stop the mininet network 
    info('*** Starting network \n')
    net.start()

    info('*** Running CLI \n')
    # CLI(net)
    net.pingAll()

    info('*** Stopping network \n')
    net.stop()   
    
    cleanup()

if __name__ == '__main__':
    setLogLevel( 'info' )
    treeTopo()
