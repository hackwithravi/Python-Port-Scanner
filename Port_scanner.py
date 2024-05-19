import socket
import threading
import argparse
import ipaddress

# Dictionary mapping ports to services
PORT_SERVICES = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    88: "Kerberos",
    110: "POP3",
    115: "SFTP",
    119: "NNTP",
    123: "NTP",
    135: "Microsoft RPC",
    137: "NetBIOS",
    139: "NetBIOS",
    143: "IMAP",
    145: "IBM NetBIOS",
    161: "SNMP",
    194: "IRC",
    443: "HTTPS",
    465: "SMTPS",
    993: "IMAPS",
    995: "POP3S",
    1433: "MSSQL",
    1521: "Oracle",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    5900: "VNC",
    8080: "HTTP Alt",
    8443: "HTTPS Alt",
    3300: "MySQL Database",
    5433: "Oracle Database",
    5984: "CouchDB",
    6667: "IRC",
    9000: "Elasticsearch",
    27017: "MongoDB",
    6379: "Redis",
    11211: "Memcached"
}

def scan_ports(host, ports, verbose=False, threads=100, service_detection=False):
    def port_scan(ip, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # Set a timeout for connection attempts
        try:
            result = sock.connect_ex((ip, port))
            if result == 0:
                if service_detection:
                    service = PORT_SERVICES.get(port, "Unknown")
                    print(f"{ip}:{port} - Open ({service})")
                elif verbose:
                    print(f"{ip}:{port} - Open")
                else:
                    print(f"{ip}:{port} - Open")
            else:
                if verbose:
                    print(f"{ip}:{port} - Closed or Filtered")
        except socket.timeout:
            if verbose:
                print(f"{ip}:{port} - Timeout")
        finally:
            sock.close()

    print(f"Scanning ports for {host}...")
    for port in ports:
        thread = threading.Thread(target=port_scan, args=(host, port))
        thread.start()
        while threading.active_count() > threads:
            pass

    for thread in threading.enumerate():
        if thread != threading.current_thread():
            thread.join()

def parse_port_range(port_range):
    if port_range == "-":
        return range(1, 65536)  # All ports
    elif "-" in port_range:
        start, end = port_range.split("-")
        return range(int(start), int(end)+1)
    else:
        return [int(port_range)]

def main():
    parser = argparse.ArgumentParser(description="Port Scanner v1.0")
    parser.add_argument("host", help="Host to scan (IP address or CIDR notation)")
    parser.add_argument("-p", "--port", help="Port range to scan (e.g., 'start_port-end_port' or '-')")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    parser.add_argument("-t", "--threads", type=int, default=100, help="Number of threads to use (default: 100)")
    parser.add_argument("-sV", "--service-detection", action="store_true", help="Enable service detection")
    parser.add_argument("-sn", "--cidr-scan", action="store_true", help="Enable CIDR scanning")
    args = parser.parse_args()

    if args.cidr_scan:
        try:
            network = ipaddress.ip_network(args.host)
        except ValueError:
            print("Invalid CIDR notation. Please provide a valid IP address or CIDR notation.")
            return

        for ip in network.hosts():
            host = str(ip)
            if args.port:
                ports = parse_port_range(args.port)
            else:
                ports = range(1, 1001)  # Default: Top 1000 ports

            scan_ports(host, ports, args.verbose, args.threads, args.service_detection)
    else:
        host = args.host
        if args.port:
            ports = parse_port_range(args.port)
        else:
            ports = range(1, 1001)  # Default: Top 1000 ports

        scan_ports(host, ports, args.verbose, args.threads, args.service_detection)

if __name__ == "__main__":
    main()
