import ftplib
from termcolor import colored as clrd #Import color text to the output, not neccessary but helps easily seeing the data


def anonLogin(ip_address): #hostname or ip address
    try:
        ftp = ftplib.FTP(ip_address)
        ftp.login("anon", "anon")
        print (clrd(f"[+] {ip_address} Anonymous FTP Login Succeeded.", "green"))
        ftp.quit()
        return True
    except Exception as e:
        print (clrd(f"[-] {ip_address} Anonymous FTP Login Failed.", "red"))

ip = input("[*] Enter Target IP: ")
anonLogin(ip)
