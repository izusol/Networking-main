import re

# calculating octect where host portion starts
def host_portion_octet(submask):
    var_oct = 0 # place holder for the octet that ranges
    for x in range(0, 33, 8):
        submask = submask - 8
        var_oct += 1
        if submask <= 0:
            break
    return var_oct
# calculate ip range interval
def calculate_increment(submask):
    for x in range(0, 5):
        if submask < 8 and submask != 0:
            increment = 2 ** (8 - submask)
            break
        elif submask == 0:
            increment = 2 ** submask
            break 
        submask = submask - 8
    return increment
# calculate network address
def calculate_network_address(ip_tuple, var_oct, inc):
    ip = list(ip_tuple) # convert to list for indexing
    var_oct = var_oct - 1
    # calculate the start of the range
    for x in range(0, 256, inc):
        if ip[var_oct] > x and ip[var_oct] < x + inc:
            ip[var_oct] = x
            break
    # set all other octets in the host portion to 0
    for x in range(1, 5 -  var_oct):
        if var_oct + 1 < 4:
            var_oct += 1
            ip[var_oct] = 0
    return ip
# calculate broadcast address
def calculate_broadcast_address(ip_tuple, var_oct, inc):
    ip = list(ip_tuple) # convert to list for indexing
    var_oct = var_oct - 1 # turn oct number to index
    # calculate the end of the range
    for x in range(0, 255, inc):
        if ip[var_oct] >= x and ip[var_oct] < x + inc:
            ip[var_oct] = x - 1 + inc # max of the current range
            break
    # set all host portion to broadcast octet
    for x in range(1, 5 -  var_oct):
        if var_oct + 1 < 4:
            var_oct += 1
            ip[var_oct] = 255
    return ip
# calculate usable range
def calculate_usable_range(net_addr, broad_addr):
    net_addr = list(net_addr)
    broad_addr = list(broad_addr)
    # for all normal cases visually the usable range is an addition and subtraction of 1 to the 4th octet of the network and broadcast address 
    net_addr[-1] = net_addr[-1] + 1
    broad_addr[-1] = broad_addr[-1] - 1

    return net_addr, broad_addr
# calculate subnet mask
def calculate_subnet_mask(cidr):
    submask = []
    for _ in range(4):
        if cidr >= 8:
            submask.append(255)
            cidr -= 8
        else:
            # Calculate the value of the partial octet 
            # e.g., a remainder of 2 bits = 11000000 in binary = 192
            partial_octet = 256 - (2 ** (8 - cidr)) if cidr > 0 else 0
            submask.append(partial_octet)
            cidr = 0
    return submask
# turns lists to string
def display(list):
    word = ".".join([str(x) for x in list])
    return word


# collect IP address and handle invalid entry
while True:
    try:
        entry = input("Enter IP/CIDR:\n")

        # split ip and cidr
        cidr = int(re.split(r'/', entry)[1])
        ip_addr = tuple([ int(x) for x in re.split(r"\.", re.split(r'/', entry)[0])]) # split ip into list of octets, convert each item into an int and convert the list into a tuple
        if 1 <= cidr <= 32 and len(ip_addr) == 4:
            check = 0 # basically a check for each octet
            for x in range(0, 4):
                if 0 <= ip_addr[x] <= 255:
                   check += 1
                else:
                    print("Invalid IP address")
            if check == 4:
                break
        else:
            print("CIDR is out of range")
    except IndexError:
        print("Enter a Valid IP in CIDR notation!!!")
    except ValueError:
        print("Enter a Valid IP in CIDR notation!!!")

# calculating host and network portion
var_octet = host_portion_octet(cidr) # place holder for the octet that ranges
increment = calculate_increment(cidr)

# calculate network address
network_address = calculate_network_address(ip_addr, var_octet, increment)
# calculate broadcast address
broadcast_address = calculate_broadcast_address(ip_addr, var_octet, increment)
# calculate usable range and total hosts
if cidr == 32:
    total_host = 1
    usable_range_lower_lim, usable_range_upper_lim = ip_addr, ip_addr
elif cidr == 31:
    total_host = 2
    usable_range_lower_lim, usable_range_upper_lim = network_address, broadcast_address
else:
    total_host = (2 ** (32 - cidr)) - 2
    usable_range_lower_lim, usable_range_upper_lim = calculate_usable_range(network_address, broadcast_address)
# calculate subnet mask
subnet_mask = calculate_subnet_mask(cidr)


print(f"IP Address: {display(list(ip_addr))}" )
print(f"Network Address: {display(network_address)}")
print(f"Broadcast Address: {display(broadcast_address)}")
print(f"Usable Range: {display(usable_range_lower_lim) + " - " + display(usable_range_upper_lim)}")
print(f"Total Host: {total_host}")
print(f"Subnet Mask: {display(subnet_mask)}")