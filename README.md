# Cybersecurity Tools coded with Python 3

Tools for cybersecurity based on Udemy course "The Complete Python Hacking Course: Beginner to Advanced" by Joseph Delgadillo where I have updated the tools to a more modern format.

## Glossary
 1 | 2
------------ | -------------
[Port Scanner](#port-scanner) | [Linux MAC Changer](#linux-mac-changer-located-in-spoofer-folder)
[Banner Grabber](#banner-grabber-located-in-portscanner-folder) | [ARP Spoofer](#arp-spoofer)
[Vulnerable Banner Scanner](#vulnerable-banner-scanner) | [Sniffer](#sniffer)
[SSH Login and Run Command](#ssh-login-and-run-command) | [DNS Query](#dns-queries)
[Bruteforce SSH Login](#bruteforce-ssh-login-located-in-sshlog-folder) |
[Anonymous FTP Login](#anonymous-ftp-login-located-in-ftp_login-folder) |
[Bruteforce FTP Login](#bruteforce-ftp-login-located-in-ftp_login-folder) |
[Hash Simple](#hash-simple) |
[Hash ForLoop](#hash-forloop-located-in-hash-folder) |
[Hash SHA1 Cracker](#hash-sha1-cracker-located-in-hash-folder) |
[Hash MD5 Cracker](#hash-md5-cracker-located-in-hash-folder) |

============================================

# **Port Scanner**
```
Features:
Multiport Scanning for a single IP Address or Host Name
Arguement Handling

Example:
------------------------------------------------------------
./portscanner_clean.py --help
------------------------------------------------------------
Usage of program: -H <target host> -p <target port>

optional arguments:
  -h, --help    show this help message and exit
  -H , --Host   Specify Target Host.
  -p , --Port   Specify Target Port for multiple ports separate by comma.
------------------------------------------------------------
Changes:
Converted to Python 3
Replaced optparse (deprecated) with argparse
Colored Output
```

# **Banner Grabber** (located in portscanner folder)
```
Banner Grabbing is a technique to gather information by sending a request to a system.
If the port is open the system can reply back with information that can expose certain information.
Which will allow the attacker to build off of to find exploits or determine another route to proceed.

Changes:
Multiport scan
Uncomment #s = socket(AF_INET, SOCK_DGRAM) for UDP Banner Grab
```

# **Vulnerable Banner Scanner**
```
A port scanner that grabs the banner and checks the specified text file and tries to match the banner with known vulnerable banners.

[-] Usage: vulnscan_udemy.py <vuln filename>

Features:
Multiport Input / Scan
Colored Text Output
```

# **SSH Login and Run Command**
```
A python script ran on a windows system that SSH into a server with Host, Username, Password requested and runs a specified command.
Using Netmiko module which is a add on to paramiko enhancing certain functionalities.

------------------------------------------------------------
Example: ./sshlog
[*] Enter Target IP: 
[*] Enter SSH User: 
[*] Enter SSH Password: 
[*] Enter command to run (; for multiple commands): 
------------------------------------------------------------

Problems:
Takes a long time to connect ~7 seconds : Tried fast cli, global delay factor (WIP)
```

# **Bruteforce SSH Login** (located in sshlog folder)
```
Bruteforce password attempts on ssh login, requires file named pass.txt which will be used line by line as password.

Cons:
SSH Connection takes time to connect if correct password after researching apparently it is meant to be for reliability.

WIP:
Add input for file with password instead of hardcoding
```

# **Anonymous FTP Login** (located in ftp_login folder)
```
Attempts to login to the FTP anonymously which allows user access to the FTP without credentials besides the FTP IP Address.
```

# **Bruteforce FTP Login** (located in ftp_login folder)
```
Bruteforce FTP login attempts using a specified text file which contains the username and password in this format user:pass.

Features:
Colored Output to show success or failure

Example:
[*] Enter Target IP: 192.168.1.1
[*] Enter User:Pass File Path: userpass.txt
[@] Trying test1:test1.
[@] Trying test2:test2.
[@] Trying test3:test3.
[@] Trying msfadmin1:msfadmin1.
[@] Trying msfadmin:msfadmin.
[+] user:pass FTP Login Succeeded.
[!] test.txt doesn't exist!
```

# **Hash Simple**
```
Using builtin module hashlib to learn syntax and follow along udemy course.

Example:
[*] Enter a string to hash: test
MD5 hash value: 098f6bcd4621d373cade4e832627b4f6
SHA1 hash value: a94a8fe5ccb19ba61c4c0873d391e987982fbbd3
SHA224 hash value: 90a3ed9e32b2aaf4c61c410eb925426119e1a9dc53d4286ade99a809
SHA256 hash value: 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08
SHA512 hash value: ee26b0dd4af7e749aa1a8ee3c10ae9923f618980772e473f8819a5d4940e0db27ac185f8a0e1d5f84f88bc887fd67b143732c304cc5fa9ad8e6f57f50028a8ff
```

# **Hash ForLoop (located in hash folder)**
```
Based on Hash Simple, wanted to combine everything to a single for loop which made the code sleeker and prints the same output.

Notes:
getattr module seems to be very versatile in condensing code
getattr module does not require the dot and parenthsis to be specified
hashlib requires bytes input
```

# **Hash SHA1 Cracker (located in hash folder)**
```
Using a password list that contains the top 10000 passwords this python script will take a given SHA1 hash compute and compare it to the password list.

Features:
Colored output

Example:
[*] Enter a SHA1 Hash Value: d6955d9721560531274cb8f50ff595a9bd39d66f
[-] Password: 123456 doesn't match guess, continuing...
[-] Password: password doesn't match guess, continuing... 
[-] Password: 12345678 doesn't match guess, continuing...
[+] The password is: joshua

Password List:
https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt
```

# **Hash MD5 Cracker (located in hash folder)**
```
Using a password list from a specified file this python script will take a given MD5 hash compute and compare it to the password list.

Features:
Colored output

Example:
[*] Enter a MD5 Hash Value: d1133275ee2118be63a577af759fc052
[*] Enter the path of the password list: plist.txt
[-] Trying Password: 123456 doesn't match, continuing...
[-] Trying Password: password doesn't match, continuing...
[-] Trying Password: 12345678 doesn't match, continuing...
[-] Trying Password: qwerty doesn't match, continuing...
[+] The password is: joshua
```

# **Linux MAC Changer (located in spoofer folder)**
```
Using the command ifconfig it will replace the current MAC Address to a specified one.
```

# **ARP Spoofer**
```
Automatically spoof the MAC Address to match target and sends packets through with the scapy module.
Python script will continue to run unless interrupted and then restores the MAC Address to original state.
```

# **Sniffer**
```
A sniffer is a tool that captures the packets that passes through the network it's monitoring.
In the folder sniffer you will find two protocal sniffers FTP and HTTP which shows how easy it is to get the credentials if not properly secured.

FTP
HTTP
Incoming Packet Sniffer (for more details check the sniffer folder)
```

# **DNS Queries**
```
This script shows the DNS query exchange to resolve a FQDN to it's machine friendly IP address.

Usage:
Run Script and then refresh or go to a webpage.
My example below is refreshing a github page.

Example:
101.2.2.15 DNS Qry "b'github.com.'" 
192.168.1.21 DNS Ans "140.82.120.4" 
101.2.2.15 DNS Qry "b'github.githubassets.com.'" 
101.2.2.15 DNS Qry "b'github.githubassets.com.'" 
```



[Back To Top](#cybersecurity-tools-coded-with-python-3)
