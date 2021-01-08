# Cybersecurity Tools coded with Python 3

Tools for cybersecurity based on Udemy course "The Complete Python Hacking Course: Beginner to Advanced" by Joseph Delgadillo where I have updated the tools to a more modern format.

1. **Port Scanner**
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

1b. **Banner Grab (located in portscanner folder)**
```
Banner Grabbing is a technique to gather information by sending a request to a system.
If the port is open the system can reply back with information that can expose certain information.
Which will allow the attacker to build off of to find exploits or determine another route to proceed.

Changes:
Multiport scan
Uncomment #s = socket(AF_INET, SOCK_DGRAM) for UDP Banner Grab
```

2. **Vulnerable Banner Scanner**
```
A port scanner that grabs the banner and checks the specified text file and tries to match the banner with known vulnerable banners.

[-] Usage: vulnscan_udemy.py <vuln filename>

Features:
Multiport Input / Scan
Colored Text Output
```

3. **SSH Login and Run Command**
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

3b. **Bruteforce SSH Login** (located in sshlog folder)
```
Bruteforce password attempts on ssh login, requires file named pass.txt which will be used line by line as password.

Cons:
SSH Connection takes time to connect if correct password after researching apparently it is meant to be for reliability.
```
