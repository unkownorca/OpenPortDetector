# OpenPortDetector

The PortScanner project is a Python-based network tool designed to help users scan and discover open ports on remote hosts. It provides a simple yet effective way to check the availability and accessibility of specific ports on a target server or device. 

## Features:

- Scan for **open** TCP ports on a specified host or IP address.
- Flexible port range selection to target a single port, a range of ports, or a list of ports.
- Quickly determine the status of ports as open or closed.
- Adjustable timeout settings for better control over scanning speed.
- Detailed results display, indicating which ports are open and closed.
- User-friendly command-line interface for easy interaction.

## Installation:

1. Clone the repository to your local machine:

> git clone https://github.com/your-username/PortScanner.git

2. Navigate to the project directory:

> cd PortScanner

3. Run the scanner with the desired target host and port(s):

> python portscannercaz.py target_host target_port(s)

## Usage:

To scan a single port on a target host:

> python portscannercaz.py example.com 80

To scan a range of ports:

> python portscannercaz.py example.com 20-80

To scan multiple specific ports:

> python portscannercaz.py example.com 22 80 443

## Disclaimer:

> Port scanning without proper authorization may be subject to legal restrictions. Use this tool responsibly and only on networks and systems that you have permission to scan. The authors are not responsible for any misuse or unlawful activities involving this software.
