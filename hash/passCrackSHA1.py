 # ! https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt
# Note: Hashes password from list above using SHA1 and then tries to match to a given SHA1 hash value
# Note: If known SHA1 hash can try to match to a given list of passwords then hash them and try to match

from urllib.request import urlopen
import hashlib
from termcolor import colored as clrd #Import color text to the output, not neccessary but helps easily seeing the data


sha1hash = input("[*] Enter a SHA1 Hash Value: ")
passList = str(urlopen("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt").read(), "utf-8")

for p in passList.split("\n"):
    hashGuess = hashlib.sha1(bytes(p, "utf-8")).hexdigest()
    if hashGuess == sha1hash:
        print(clrd(f"[+] The password is: {str(p)}", "green"))
        quit()
    else:
        print(clrd(f"[-] Password: {str(p)} doesn't match guess, continuing...", "red"))
print(clrd("Password doesn't exist in this list", "orange"))
