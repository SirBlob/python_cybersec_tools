# Note: works but takes ~7 seconds to get output
from netmiko import *

ip = input("[*] Enter Target IP: ")
user = input("[*] Enter SSH User: ")
pswd = input("[*] Enter SSH Password: ")

device = { 
    #Defines the device parameters
    "device_type": "autodetect",
    "host": ip,
    "username": user,
    "password": pswd,
    "secret": pswd,
    "port": 22,
    "global_delay_factor": .1
}
#To autodetect the device type 
DETECT_DEVICE = SSHDetect(**device)
DEVICE_TYPE = DETECT_DEVICE.autodetect()

def main():
    try:
        net_connect = ConnectHandler(**device) #to use the device parameters #! for some reason takes ~7 seconds to run this
        commands = input("[*] Enter command to run (; for multiple commands): ") #what command to send
        output = net_connect.send_command(commands) #sends the command
        print(output) #prints the command output
    except Exception as e:
        print("Error: " + str(e))
    
if __name__ == "__main__":
    main()
