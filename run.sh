#!/bin/bash

# Note: Mininet must be run as root.  So invoke this shell script
# using sudo.

echo "Running bash script..."

# Block 1 host
printf "id,mac\n1,00:00:00:00:00:01" > ../../pox/pox/misc/firewall-policies.csv

# Block 2 hosts
# printf "id,mac\n1,00:00:00:00:00:03,\n2,00:00:00:00:00:07" > ../../pox/pox/misc/firewall-policies.csv

# Block 3 hosts
# printf "id,mac\n1,00:00:00:00:00:02\n2,00:00:00:00:00:04\n3,00:00:00:00:00:08" > ../../pox/pox/misc/firewall-policies.csv

# Run sdn.py
gnome-terminal --tab --command="bash -c '~/pox/pox.py forwarding.l2_learning misc.firewall; $SHELL'"
sudo python sdn.py

echo "Done!"
