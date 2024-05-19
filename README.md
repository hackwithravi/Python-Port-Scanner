Python Port Scanner
Description

Python Port Scanner is an advanced network scanning tool implemented in Python. It provides various scanning techniques such as TCP, UDP, SYN, Ping, Xmas, and Aggressive scans. The script is multi-threaded for faster scanning and utilizes the socket and subprocess modules for network communication and service detection.
Features

    TCP connect scan
    UDP scan
    TCP SYN scan (-sS)
    Ping Scan (-sn)
    Xmas Scan
    Aggressive Scan
    Multi-threaded scanning
    Verbose output option

Requirements

    Python 3
    Nmap (for service detection)

Installation


    git clone https://github.com/your_username/python-port-scanner.git

Install the required Python dependencies:

    pip install -r requirements.txt

Usage

bash

        usage: port_scanner.py [-h] [-s] [-e] [-t] [-V] [--tcp] [--udp] [--syn] [--ping] [--xmas] [--aggressive] [-v]
                       target

Advanced Port Scanner Based on Python

positional arguments:
  target             IP or hostname to scan

optional arguments:
  -h, --help         show this help message and exit
  -s , --start       start port number (default: 1)
  -e , --end         end port number (default: 65535)
  -t , --threads     threads use (default: 1000)
  -V, --verbose      verbose output
  --tcp              perform TCP scan (default)
  --udp              perform UDP scan
  --syn              perform TCP SYN scan (-sS)
  --ping             perform Ping Scan (-sn)
  --xmas             perform Xmas Scan
  --aggressive       perform Aggressive Scan
  -v, --version      display version

Example:
python port_scanner.py example.com --tcp --verbose

Examples

    Perform a TCP scan on ports 1-1000 with verbose output:

    python port_scanner.py example.com --tcp --start 1 --end 1000 --verbose

Perform an Aggressive Scan with default port range:

    python port_scanner.py example.com --aggressive

License

This project is licensed under the MIT License - see the LICENSE file for details.

Author

Ravi
