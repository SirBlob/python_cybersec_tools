# Cybersecurity Tools coded with Python 3

Tools for cybersecurity based on Udemy course "The Complete Python Hacking Course: Beginner to Advanced" by Joseph Delgadillo where I have updated the tools to a more modern format.

## Glossary
1. [Port Scanner](#port-scanner)
2. [Banner Grabber](#banner-grabber-located-in-portscanner-folder)
3. [Vulnerable Banner Scanner](#vulnerable-banner-scanner)
4. [SSH Login and Run Command](#ssh-login-and-run-command)
5. [Bruteforce SSH Login](#bruteforce-ssh-login-located-in-sshlog-folder)
6. [Anonymous FTP Login](#anonymous-ftp-login-located-in-ftp_login-folder)
7. [Bruteforce FTP Login](#bruteforce-ftp-login-located-in-ftp_login-folder)
8. [Hash Simple](#hash-simple)
9. [Hash ForLoop](#hash-forloop-located-in-hash-folder)

============================================

# **Port Scanner**
```
Features:
Multiport Scanning for a single IP Address or Host Name
Arguement Handling

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
./sshlog
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

[Back To Top](#cybersecurity-tools-coded-with-python-3)
