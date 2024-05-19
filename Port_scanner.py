#!/usr/bin/python3
from argparse import ArgumentParser
import socket
from threading import Thread
from time import time
import subprocess

open_ports = {}
open_services = {}

def prepare_args():
    """
    Prepare arguments 
    return:
        args(argparse.Namespace)
    """
    parser = ArgumentParser(description="Advanced Port Scanner Based on Python", usage="%(prog)s 192.168.1.2", epilog="Example - %(prog)s -s 20 -e 40000 -t 500 -V 192.168.1.2")
    parser.add_argument(metavar="IPv4", dest="target", help="IP or hostname to scan")
    parser.add_argument("-s", "--start", dest="start", metavar="", type=int, help="start port number", default=1)
    parser.add_argument("-e", "--end", dest="end", metavar="", type=int, help="end port number", default=65535)
    parser.add_argument("-t", "--threads", dest="threads", metavar="", type=int, help="threads use", default=1000)
    parser.add_argument("-V", "--verbose", dest="verbose", action="store_true", help="verbose output")
    parser.add_argument("--tcp", dest="tcp_scan", action="store_true", help="perform TCP scan (default)")
    parser.add_argument("--udp", dest="udp_scan", action="store_true", help="perform UDP scan")
    parser.add_argument("--syn", dest="syn_scan", action="store_true", help="perform TCP SYN scan (-sS)")
    parser.add_argument("--ping", dest="ping_scan", action="store_true", help="perform Ping Scan (-sn)")
    parser.add_argument("--xmas", dest="xmas_scan", action="store_true", help="perform Xmas Scan")
    parser.add_argument("--aggressive", dest="aggressive_scan", action="store_true", help="perform Aggressive Scan")
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 1.0", help="display version")
    args = parser.parse_args()
    return args

def prepare_ports(start:int, end:int):
    """
    generator function for port
    """
    for port in range(start, end + 1):
        yield port

def tcp_scan(target, ports):
    """
    Perform TCP connect scan
    """
    while True:
        try:
            port = next(ports)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            result = s.connect_ex((target, port))
            if result == 0:
                open_ports[port] = 'open'
                if arguments.verbose:
                    service_info = subprocess.check_output(f"nmap -sV -p {port} {target}", shell=True).decode()
                    for line in service_info.split("\n"):
                        if "service" in line:
                            service_name = line.split("/")[3].strip()
                            open_services[port] = service_name
                            if arguments.verbose:
                                print(f"Port {port} is open: {service_name}")
            s.close()
        except StopIteration:
            break

def udp_scan(target, ports):
    """
    Perform UDP scan
    """
    while True:
        try:
            port = next(ports)
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.settimeout(2)
            s.sendto(b'', (target, port))
            data, _ = s.recvfrom(1024)
            open_ports[port] = 'open'
            if arguments.verbose:
                service_info = subprocess.check_output(f"nmap -sV -p {port} {target}", shell=True).decode()
                for line in service_info.split("\n"):
                    if "service" in line:
                        service_name = line.split("/")[3].strip()
                        open_services[port] = service_name
                        if arguments.verbose:
                            print(f"Port {port} is open: {service_name}")
            s.close()
        except (socket.timeout, ConnectionRefusedError):
            open_ports[port] = 'closed'
        except StopIteration:
            break

def syn_scan(target, ports):
    """
    Perform TCP SYN scan (-sS)
    """
    while True:
        try:
            port = next(ports)
            s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
            s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
            s.settimeout(2)
            s.connect_ex((target, port))
            open_ports[port] = 'open'
            if arguments.verbose:
                service_info = subprocess.check_output(f"nmap -sV -p {port} {target}", shell=True).decode()
                for line in service_info.split("\n"):
                    if "service" in line:
                        service_name = line.split("/")[3].strip()
                        open_services[port] = service_name
                        if arguments.verbose:
                            print(f"Port {port} is open: {service_name}")
            s.close()
        except (socket.timeout, ConnectionRefusedError):
            open_ports[port] = 'closed'
        except StopIteration:
            break

def ping_scan(target):
    """
    Perform Ping Scan (-sn)
    """
    try:
        subprocess.run(f"nmap -sn {target}", shell=True, check=True)
    except subprocess.CalledProcessError:
        print("Error: Ping scan failed.")

def xmas_scan(target, ports):
    """
    Perform Xmas Scan
    """
    try:
        subprocess.run(f"nmap -sX {target}", shell=True, check=True)
    except subprocess.CalledProcessError:
        print("Error: Xmas scan failed.")

def aggressive_scan(target):
    """
    Perform Aggressive Scan
    """
    try:
        subprocess.run(f"nmap -A {target}", shell=True, check=True)
    except subprocess.CalledProcessError:
        print("Error: Aggressive scan failed.")

def prepare_threads(scan_func, threads:int):
    """
    Create and start threads 
    Arguments:
        threads(int): Number of threads to use
    """
    threads_list = []
    for _ in range(threads + 1):
        threads_list.append(Thread(target=scan_func, args=("example.com", ports)))  # <-- Here
    for thread in threads_list:
        thread.start()
    for thread in threads_list:
        thread.join()

if __name__ == "__main__":
    arguments = prepare_args()
    ports = prepare_ports(arguments.start, arguments.end)
    start_time = time()
    
    # Select scan function based on user input
    if arguments.udp_scan:
        scan_func = udp_scan
    elif arguments.syn_scan:
        scan_func = syn_scan
    elif arguments.ping_scan:
        ping_scan("example.com")  # <-- Here
        exit()
    elif arguments.xmas_scan:
        xmas_scan("example.com", ports)  # <-- Here
        exit()
    elif arguments.aggressive_scan:
        aggressive_scan("example.com")  # <-- Here
        exit()
    else:
        scan_func = tcp_scan
    
    prepare_threads(scan_func, arguments.threads)
    end_time = time()
    
    print(f"Scan took {end_time - start_time} seconds")
    
    if open_ports:
        print("Open ports:")
        for port, status in open_ports.items():
            print(f"Port {port}: {status}")
        if open_services:
            print("Open services:")
            for port, service in open_services.items():
                print(f"Port {port}: {service}")
    else:
        print("No open ports found.")
