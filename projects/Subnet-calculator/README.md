Subnet Calculator (CLI Tool)

Description: The Subnet Calculator is a tool that takes in an IP address in CIDR notation and calculates the Network Address, Broadcast Address, Usable Range, Total Host and Subnet Mask

Features

- Parses IP/CIDR input
- Calculates network address
- Calculates broadcast address
- Shows usable host range
- Validates input

How to Run
python main.py

Example:
c:\> python main.py
Enter IP/CIDR:
192.168.1.10/24

IP Address: 192.168.1.10
Network Address: 192.168.1.0
Broadcast Address: 192.168.1.255
Usable Range: 192.168.1.1 - 192.168.1.254
Total Host: 254
Subnet Mask: 255.255.255.0

What I Learned:
In this project I made an effort to use as little abstraction as possible so that I could have a deeper understanding of subnetting logic and how to implement it programatically.

Future Improvements:

- use Python ipaddress module
- add GUI or web version
- improve subnet mask accuracy
- refactor logic

What is broken:

- subnet mask is incomplete for non-/8,/16,/24 cases
