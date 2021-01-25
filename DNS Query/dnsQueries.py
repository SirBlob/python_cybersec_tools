#!/usr/bin/python3
from scapy.all import *

def findDNS(p):
    if p.haslayer(DNS):
        print(p[IP].src, p[DNS].summary())
        
sniff(prn=findDNS)
