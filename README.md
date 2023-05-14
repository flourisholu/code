# eee4121f-b-lab2
## Part 1

### Make files executable
1. Run 'chmod +x sdn.py' to make the sdn.py file executable.
2. Run 'chmod +x run.sh' to make the sdn.py file executable.

### Run the experiments
For Experiment 1:
1. Run 'sudo ./run.sh' to run the experiment where only host H1 is blocked
2. Exit the terminal that opens up once the script is done running and use 'Ctrl +C' to exit Mininet.

For Experiment 2:
1. Kill all processes by running 'sudo mn -c'. You may also need to run 'sudo fuser -k 6633/tcp' (where 6633 is the port where the controller is running) so that the controller port is cleared.
2. In the 'run.sh' bash script, comment out the line under '# Block 1 host' and uncomment the line under '#Block 2 hosts'
3. Exit the terminal that opens up once the script is done running and use 'Ctrl +C' to exit Mininet.
4. Run 'sudo ./run.sh' to run the experiment where hosts H3 and H7 are blocked

For Experiment 3:
1. Kill all processes by running 'sudo mn -c'. You may also need to run 'sudo fuser -k 6633/tcp' (where 6633 is the port where the controller is running) so that the controller port is cleared.
2. In the 'run.sh' bash script, comment out the line under '# Block 2 hosts' and uncomment the line under '#Block 3 hosts'
3. Exit the terminal that opens up once the script is done running and use 'Ctrl +C' to exit Mininet.
4. Run 'sudo ./run.sh' to run the experiment where hosts H2, H4, and H8 are blocked

