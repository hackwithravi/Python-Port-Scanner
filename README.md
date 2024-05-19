# Port Scanner

## Description
A simple Python script to scan ports on a host or a range of hosts using threading. The script allows scanning specific ports or a range of ports, and it supports service detection for known ports.

## Features
- Scan ports on a single host or a range of hosts using CIDR notation
- Specify specific ports or port ranges to scan
- Enable service detection for known ports
- Multi-threaded scanning for faster results

## Requirements
- Python 3

## Usage
### Arguments
- `host`: The host to scan (IP address or CIDR notation)
- `-p PORT, --port PORT`: Port range to scan (e.g., 'start_port-end_port' or '-'). Default: Top 1000 ports.
- `-v, --verbose`: Enable verbose output
- `-t THREADS, --threads THREADS`: Number of threads to use for scanning (default: 100)
- `-sV, --service-detection`: Enable service detection
- `-sn, --cidr-scan`: Enable CIDR scanning (specify a range of IP addresses)

## Examples
- Scan top 1000 ports on a single host:

Installation

  
    git clone https://github.com/hackwithravi/Python-Port-Scanner.git

    cd Python-Port-Scanner

    chmod +x Port_scanner.py





Run the script with Python3:



    python3 Port_scanner.py example.com <arguments>

Version 1.0

License

This project is licensed under the MIT License. See the LICENSE file for details.

Credits

https://github.com/hackwithravi
