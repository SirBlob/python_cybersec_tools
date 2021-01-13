import subprocess

def changeMAC(iface, mac):
    subprocess.call(["ifconfig " + iface + " down"]) # ! Calls commond ifconfig [interface] down
    subprocess.call(["ifconfig " + iface + " hw " + "ether " + mac]) # ! Calls commond ifconfig [interface] hw ether [mac]
    subprocess.call(["ifconfig " + iface + " up"]) # ! Calls commond ifconfig [interface] up

def main():
    iface = input("[*] Enter Interface of MAC Address to Change: ")
    newMA = input("[*] ENter New MAC Address: ")

    initial = subprocess.check_output(["ifconfig " + iface]) # Note: only works on Linux machines, windows need ipconfig
    changeMAC(iface, newMA)
    final = subprocess.check_output(["ifconfig " + iface])
    if initial == final:
        print(f"[-] Failed to change MAC Address to {newMA}")
    else:
        print(f"[+] Successfully changed MAC Address: {newMA} on Interface: {iface}")

if __name__ == "__main__":
    main()
