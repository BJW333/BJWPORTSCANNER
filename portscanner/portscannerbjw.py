from socket import *
import sys
import time
import socket
import random
import os
import threading
import argparse

print('''Welcome to PortScanner would you like me to start the tool
        [1] start
        [99] exit
''')

starttool = input('Your choice here: ')
if starttool == "1":
    print('Starting Tool')
    time.sleep(2)
    
if starttool == "99":
        time.sleep(1)
        print("Shuting Down")
        exit()
    
def conScan(tgtHost, tgtPort):
    try:
        connskt = socket(AF_INET, SOCK_STREAM)
        connskt.connect((tgtHost, tgtPort))
        print('[+]%d/tcp open'% tgtPort)
        connskt.close()
    except:
        print('[-]%d/tcp closed'% tgtPort)
        
def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print('[-] Cannot resolve %s '% tgtHost)
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print('\n[+] Scan result of: %s ' % tgtName[0])
    except:
        print('\n[+] Scan result of: %s ' % tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print('Scanning Port: %s'% tgtPort)
        conScan(tgtHost, int(tgtPort))

if __name__ == '__main__':
    print('What is the ip you want to scan')
    ip = input("[*] target ip for scan : ")
    time.sleep(1)
    print('What is the ip you want to scan')
    port = input("[*] target port for scan : ") 
    time.sleep(1)
    portScan(ip, [port])
