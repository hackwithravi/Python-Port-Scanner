# Simple-Port-Scanner-
Python based  Port Scanner
Features

    Scan a range of ports on a specified IP address or hostname.
    Multi-threaded scanning for faster results.
    Detection of open ports and services running on those ports.

Usage

    Clone the Repository:
    
    git clone https://github.com/your_username/advanced-port-scanner.git
    cd advanced-port-scanner

    Install Dependencies:
    
    pip install -r requirements.txt
    Run the Script:
    python port_scanner.py target_ip_or_hostname

Replace port_scanner.py with the name of the Python script and target_ip_or_hostname with the IP address or hostname you want to scan.

Options:

    -s, --start: Start port number (default: 1).
    -e, --end: End port number (default: 65535).
    -t, --threads: Number of threads to use (default: 1000).
    -V, --verbose: Enable verbose output.

Example:

bash

    python port_scanner.py -s 20 -e 40000 -t 500 -V 192.168.1.2

    This command scans ports from 20 to 40000 on the IP address 192.168.1.2 using 500 threads and verbose output.

Dependencies

    argparse: Used for parsing command-line arguments.
    nmap: Used for service detection on open ports.
