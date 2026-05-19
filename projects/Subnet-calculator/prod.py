import ipaddress

# collect IP address and handle invalid entry
while True:
    entry = input("Enter IP/CIDR:\n")
    try:
        
        net = ipaddress.IPv4Network(entry, strict=False)
        ip = ipaddress.IPv4Interface(entry)
        break
    except ValueError:
        print("Enter a Valid IP in CIDR notation!!!")

# Calculate Usable Range and Hosts
if net.prefixlen == 32:
    usable_range = f"{ip.ip} - {ip.ip}"
    total_host = 1
elif net.prefixlen == 31:
    usable_range = f"{net.network_address} - {net.broadcast_address}"
    total_host = 2
else:
    # .hosts() generates all usable IPs in the subnet
    hosts = list(net.hosts()) 
    usable_range = f"{hosts[0]} - {hosts[-1]}"
    total_host = net.num_addresses - 2

# Output
print(f"IP Address: {ip.ip}")
print(f"Network Address: {net.network_address}")
print(f"Broadcast Address: {net.broadcast_address}")
print(f"Usable Range: {usable_range}")
print(f"Total Host: {total_host}")
print(f"Subnet Mask: {net.netmask}")