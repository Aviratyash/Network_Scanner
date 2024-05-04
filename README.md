# Network Scanner

This Python script is designed to scan a network for active hosts and open ports. It provides information about devices connected to the network and their respective open ports.

## Features

- Discover active hosts on a network.
- Identify open ports on discovered hosts.
- Provide detailed information about each active host and its open ports.

## How it Works

The network scanner utilizes various network scanning techniques, such as ICMP ping sweeps and TCP port scans, to identify active hosts and open ports. It employs multi-threading for efficient scanning and socket programming for port scanning.

## Usage

To use the network scanner, follow these steps:

1. Clone the repository or download the `network_scanner.pyw` script.
2. Run the script by executing the following command in your terminal:

```bash
python network_scanner.py -t <target_ip_range>
```
OR
1. Use the executable(.exe) version of the script.
