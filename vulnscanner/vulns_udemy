from socket import *
import os
import sys
from termcolor import colored as clrd #Import color text to the output, not neccessary but helps easily seeing the data

def returnBan(ip, port): #Socket module connect and returns banner
    try:
        setdefaulttimeout(2)
        s = socket(AF_INET, SOCK_STREAM) #TCP
        #s = socket(AF_INET, SOCK_DGRAM) #UDP
        s.connect((ip, port))
        banner = s.recv(1024) #Store the 1024 bytes in the variable banner
        s.close()
        return banner
    except:
        print(f"Cannot connect to port: {port}")
        return

def checkVulns(banner, filename): #Compares vulnerability defined in filename to banner 
    fn = open(filename, "rb")
    for line in fn.readlines():
        if line in banner: #strip seems to be a problem
            print (clrd("[++] Server is vulnerable: " + banner.decode("utf-8"), "red"))

def main():
    if len(sys.argv) == 2: #requires 2 arguements
        filename = sys.argv[1] #python starts at 0, 1
        if not os.path.isfile(filename): #if the file doesn't exist
            print ("[-] File Doesn't Exist!")
            exit(0)
        if not os.access(filename, os.R_OK): #if higher privilege is needed
            print ("[-] Access Denied.")
            exit(0)
    else:
        print (f"[-] Usage: {str(sys.argv[0])} <vuln filename>") #if no argument shows this when running
        exit(0)

    portlist= []
    ip = input("[*] Enter Target IP: ")
    portlist = [port for port in input("[*] Enter Target Port: ").split(",")] #list comprehension for multiple port inputs
    for port in portlist:
        banner = returnBan(ip, int(port))
        if banner:
            print(clrd(f"[+] {ip}:{port} : " + banner.decode("utf-8"), 'green'))
            checkVulns(banner, filename)

if __name__ == "__main__":
    main()
