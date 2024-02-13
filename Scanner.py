#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print("Welcome, this is a simple nmap automation tool")
print("<-------------------------------------------->")

ip_address = input("Enter the IP address to scan: ")
print("The IP you entered is: ", ip_address)
type(ip_address)

resp = input("""\nPlease enter h type of scan you want to run
             1) SYN ACK Scan
             2)UDP Scan
             3)Comprehensive Scan \n""")
print("You have selected opion: ", resp)

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_address, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ",scanner[ip_address].state())
    print(scanner[ip_address].all_protocols(), "\n")  # Print all protocols
    print("Open Ports: ", scanner[ip_address]['tcp'].keys())   #Print open ports with their number
elif resp == '2':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_address, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("Ip Status: ",scanner[ip_address].state())
    print(scanner[ip_address].all_protocols(), "\n")  # Print all protocols
    print("Open Ports: ", scanner[ip_address]['udp'].keys())   #Print open ports with their number
elif resp == '3':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_address, '1-1024', '-v -sV -sS -sC -A -O')
    print(scanner.scaninfo())
    print("Ip Status: ",scanner[ip_address].state())
    print(scanner[ip_address].all_protocols(), "\n")  # Print all protocols
    print("Open Ports: ", scanner[ip_address]['tcp'].keys())   #Print open ports with their number
elif resp >= '4':
    print("Please enter a valid option")