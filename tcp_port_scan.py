from scapy.all import *
#Define the target IP address and the range of ports to scan
target_ip='192.168.149.128'
port_range=range(1,100)
#Loop through the po3rts and send a TCP SYN packet to each one
for port in port_range:
    pckt=IP(dst=target_ip)/TCP(dport=port,flags="S")
    res=sr1(pckt,timeout=1,verbose=0)
    if res is not None:
        print("port {} is open ".format(port))