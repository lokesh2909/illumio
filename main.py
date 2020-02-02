# -*- coding: utf-8 -*-

import csv

def main():
    try:
        # Open a the output file 
        file = open('output.txt','a')
        # Open the input csv file
        with open('data.csv', newline='') as csvfile:
            inputreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            inputreader = list(inputreader)
            # Loop through the entire list of data in the input file
            for row in inputreader:
                print(row[0])
                # Split the entry into the corresponding direction, protocol,
                # port and Ip address
                intermediate = row[0].split(",")
                direction = intermediate[0]
                protocol = intermediate[1]
                port = intermediate[2]
                ip_address = intermediate[3]
                # Call the accept_packet function to find out the valid output
                result = accept_packet(direction,protocol,port,ip_address)
                print(result)
                # As additional backup write the output to a text file
                file.write(str(result)+'\n')
    except:
        print("Please specify the correct path of the file") 
    
    file.close()
    
def convert_ipv4(ip):
  return tuple(int(n) for n in ip.split('.'))
        
def accept_packet(direction,protocol,port,ip_address):
    
    if(direction == "inbound"):
        if(protocol == "tcp"):
            if(port == "80"):
                if(ip_address == "192.168.1.2"):
                    return True
                else:
                    return False
            else:
                return False
        elif(protocol == "udp"):
            if(port == "53"):             
                if(convert_ipv4("192.168.1.1") < convert_ipv4(ip_address) < convert_ipv4("192.168.2.5")):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    elif(direction == "outbound"):
        if(protocol == "tcp"):
            if(10000 <= int(port) <= 20000):
                if(ip_address == "192.168.10.11"):
                    return True
                else:
                    return False
            else:
                return False
        elif(protocol =="udp"):
            if(1000 <= int(port) <= 2000):
                if(ip_address == "52.12.48.92"):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
    
if __name__ == "__main__":
    main()