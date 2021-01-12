 #! Requires MD5 hash and passwordlist.txt
 # Note: given a MD5 hash and a passwordlist it will hash the list of passwords till it matches the MD5 hash

import hashlib
from termcolor import colored as clrd #Import color text to the output, not neccessary but helps easily seeing the data

def file_status(passList):
    global passFile
    try:
        passFile = open(passList, "r")
    except:
        print(clrd("File doesn't exist in this path.", "blue"))
        exit(0)

md5hash = input("[*] Enter a MD5 Hash Value: ")
passList = input("[*] Enter the path of the password list: ")

file_status(passList)
for p in passFile:
    print(clrd(f"[-] Trying Password: {str(p.strip())} doesn't match, continuing...", "red"))
    enc_pass = p.encode("utf-8")
    hashGuess = hashlib.md5(enc_pass.strip()).hexdigest()

    if hashGuess == md5hash:
        print(clrd(f"[+] The password is: {str(p)}", "green"))
        passFile.close() #don't need as the exit would do the same thing
        exit(0)

print(clrd(f"[-] Password doesn't exist in list.", "red"))
