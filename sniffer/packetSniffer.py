#!/usr/bin/python3 #works on linux

import socket
import os, sys
import struct
import binascii

sock_created = False
sniffer_socket = 0

#http://www.tcpipguide.com/free/t_UDPMessageFormat.htm
def analyze_udp_header(data_recv): 
    udp_hdr = struct.unpack("!4H", data_recv[:8])
    src_port = udp_hdr[0]
    dst_port = udp_hdr[1]
    length = udp_hdr[2]
    chksum = udp_hdr[3]
    data = data_recv[8:]

    print("------------------------UDP HEADER------------------------")
    print(f"Source Port: {src_port}")
    print(f"Destination Port: {dst_port}")
    print(f"Length: {length}")
    print(f"Check Sum: {chksum}")

    return data

#https://www.gatevidyalay.com/transmission-control-protocol-tcp-header/
def analyze_tcp_header(data_recv):
    tcp_hdr = struct.unpack("2H2I4H", data_recv[:20])
    src_port = tcp_hdr[0]
    dst_port = tcp_hdr[1]
    seq_num = tcp_hdr[2]
    ack_num = tcp_hdr[3]
    data_offset = tcp_hdr[4] >> 12
    reserved = (tcp_hdr[5] >> 6) & 0x03ff
    flags = tcp_hdr[4] & 0x003f
    window = tcp_hdr[5]
    chksum = tcp_hdr[6]
    urg_ptr = tcp_hdr[7]
    data = data_recv[20:]

    urg = bool(flags & 0x0020)
    ack = bool(flags & 0x0010)
    psh = bool(flags & 0x0008)
    rst = bool(flags & 0x0004)
    syn = bool(flags & 0x0002)
    fin = bool(flags & 0x0001)

    print("------------------------TCP HEADER------------------------")
    print(f"Source Port: {src_port}")
    print(f"Destination Port: {dst_port}")
    print(f"Sequence Number: {seq_num}")
    print(f"Acknowledge Number: {ack_num}")
    print(f"Data Offset: {data_offset}")
    print(f"Reserved: {reserved}")

    print(f"===Flags=== ")
    print(f"URG: {urg}")
    print(f"ACK: {ack}")
    print(f"PUSH: {psh}")
    print(f"RESET: {rst}")
    print(f"SYNCHRONIZE: {syn}")
    print(f"FINISH: {fin}")
    print(f"Window Size: {window}")
    print(f"CheckSum: {chksum}")
    #print(f"Urg Pointer: {urg_ptr}")

    return data

#https://en.wikipedia.org/wiki/IPv4#/media/File:IPv4_Packet_-en.svg
def analyze_ip_header(data_recv):
    ip_hdr = struct.unpack("!6H4s4s", data_recv[:20])
    ver = ip_hdr[0] >> 12
    ihl = (ip_hdr[0] >> 8) & 0x0f
    tos = ip_hdr[0] & 0x00ff
    total_len = ip_hdr[1]
    ip_id = ip_hdr[2]
    flags = ip_hdr[3] >> 13
    frag_off = ip_hdr[3] & 0x1fff
    ip_ttl = ip_hdr[4] >> 8
    ip_proto = ip_hdr[4] & 0x00ff
    chksum = ip_hdr[5]
    src_addr = socket.inet_ntoa(ip_hdr[6])
    dst_addr = socket.inet_ntoa(ip_hdr[7])
    data = data_recv[20:]

    print("------------------------IP HEADER------------------------")
    print(f"Version: {ver}")
    print(f"IHL: {ihl}")
    print(f"TOS: {tos}")
    print(f"Total Length: {total_len}")
    print(f"IP ID: {ip_id}")
    print(f"Flags: {flags}")
    print(f"Frags Offset: {frag_off}")
    print(f"IP TTL: {ip_ttl}")
    print(f"IP Protocol: {ip_proto}")
    print(f"CheckSum: {chksum}")
    print(f"Source Address: {src_addr}")
    print(f"Destination Address: {dst_addr}")

    if ip_proto == 6:
        tcp_udp = "TCP"
    elif ip_proto == 17:
        tcp_udp = "UDP"
    else:
        tcp_udp = "Other"
    return data, tcp_udp

#https://www.gatevidyalay.com/ethernet-ethernet-frame-format/
def analyze_ether_header(data_recv):
    ip_bool = False

    eth_header = struct.unpack("!6s6sH", data_recv[:14]) #format string and first 14 bytes
    dest_mac = binascii.hexlify(eth_header[0]).decode("utf-8") #decode otherwise prints bytes
    src_mac = binascii.hexlify(eth_header[1]).decode("utf-8")
    proto = eth_header[2] >> 8 #ipv4
    data = data_recv[14:]
    print("------------------------ETHERNET HEADER------------------------")
    print(f"Destination MAC: {dest_mac[0:2]}:{dest_mac[2:4]}:{dest_mac[4:6]}:{dest_mac[6:8]}:{dest_mac[8:10]}:{dest_mac[10:12]}")
    print(f"Source MAC: {src_mac[0:2]}:{src_mac[2:4]}:{src_mac[4:6]}:{src_mac[6:8]}:{src_mac[8:10]}:{src_mac[10:12]}")
    print(f"Protocol: {proto}")
    if proto == 0x08:
        ip_bool = True
    return data, ip_bool

def main():
    global sock_created
    global sniffer_socket
    if sock_created == False:
        sniffer_socket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0003)) #host to network short 
        sock_created = True

    data_recv = sniffer_socket.recv(2048)
    os.system("clear")

    data_recv, ip_bool = analyze_ether_header(data_recv)
    if ip_bool:
        data_recv, tcp_udp = analyze_ip_header(data_recv)
    else:
        return

    if tcp_udp == "TCP":
        data_recv = analyze_tcp_header(data_recv)
    elif tcp_udp == "UDP":
        data_recv = analyze_udp_header(data_recv)
    else:
        return
while True:
    try:
        main()
    except KeyboardInterrupt:
        exit(0)