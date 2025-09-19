'''
A valid IPv4 address consists of four integer numbers separated by dots (.). 
Each number must satisfy the following conditions:
    It is between 0 and 255 inclusive.
    It does not have leading zeros (e.g. 0 is allowed, 01 is not).
    Only numeric characters are allowed.
'''
def is_valid_ipv4(ipv4):
    new_ipv4 = ipv4.split(".")
    valid = []
    if len(new_ipv4) == 4:
        for number in new_ipv4:
            if number.isdigit() and 0 <= int(number) <= 255:
                    if len(number) > 1 and number.startswith('0'):
                        valid.append(False)
                    else:
                        valid.append(True)
            else:
                valid.append(False)
    else: 
        return False
    if False in valid:
        return False
    else:
        return True
print(f"{is_valid_ipv4("192.168.0.30")}") #should return True.
print(f"{is_valid_ipv4("192.168.1.1")}") #should return True.
print(f"{is_valid_ipv4("0.0.0.0")}") #should return True.
print(f"{is_valid_ipv4("255.01.50.111")}") #should return False.
print(f"{is_valid_ipv4("255.00.50.111")}") #should return False.
print(f"{is_valid_ipv4("256.101.50.115")}") #should return False.
print(f"{is_valid_ipv4("192.168.101.")}") #should return False.
print(f"{is_valid_ipv4("192168145213")}") #should return False.
