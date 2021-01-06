from socket import *

def returnBan(ip, port):
    try:
        setdefaulttimeout(2)
        s = socket(AF_INET, SOCK_STREAM) #TCP
        #s = socket(AF_INET, SOCK_DGRAM) #UDP
        s.connect((ip, port))
        s.send('GET HTTP/1.1 \r\n')
        banner = s.recv(1024) #Store the 1024 bytes in the variable banner
        s.close()
        return banner
    except:
        print(f"Cannot connect to port: {port}")
        return

def main():
    portlist= []
    ip = input("[*] Enter Target IP: ")
    portlist = [port for port in input("[*] Enter Target Port: ").split(",")] #list comprehension for multiple port inputs
    for port in portlist:
        banner = returnBan(ip, int(port))
        if banner:
            print(f"[+] {ip}:{port} : {banner}")

if __name__ == "__main__":
    main()
