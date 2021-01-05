# ! Requires python 3.6 and up

from socket import  * #Imports everything from socket library
from threading import * #Imports everything from threading library
import argparse as argp #Import argparse as argp for arguement parsing
from termcolor import colored as clrd #Import color text to the output, not neccessary but helps easily seeing the data

def connScan(tgtHost, tgtPort): # Note: Does the port scanning
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((tgtHost, tgtPort))
        print(clrd(f"[+] Port {tgtPort} for tcp is Open", 'green'))
    except:
        print(clrd(f"[-] Port {tgtPort} for tcp is Closed", 'red'))
    finally:
        sock.close()

def portScan(tgtHost, tgtPorts): # Note: Does the Parsing and Threading if multiple ports
    try:
        tgtIP = gethostbyname(tgtHost) 
    except:
        print (f"Unknown Host {tgtHost} ")

    try:
        tgtName = gethostbyaddr(tgtIP)
        print (f"Scan Results for: {tgtName[0]}")
    except:
        print (f"Scan Results for: {tgtIP}")
    setdefaulttimeout(1) 
    for tgtPort in tgtPorts: 
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort))) 
        t.start()

def main():
    parser = argp.ArgumentParser(description="Usage of program: " + "-H <target host> -p <target port>")
    parser.add_argument("-H", "--Host", dest="tgtHost", metavar="", required=True, help="Specify Target Host.")
    parser.add_argument("-p", "--Port", dest="tgtPort", metavar="", required=True, help="Specify Target Port for multiple ports separate by comma.")
    options = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(",")

    if (tgtHost == None) | (tgtPorts[0] == None):
        print(clrd(parser.usage, 'cyan'))
        # Note: Outputs "Usage of program: -H <target host> -p <target port>" if no parameters attached
        exit(0)
    portScan(tgtHost, tgtPorts)

if __name__ == "__main__":
    main()
