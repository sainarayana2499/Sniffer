from scapy.all import *;
def sniffer(pkt):
	print("Source IP:%s DestIP:%s"%(pkt[IP].src,pkt[IP].dst))
a=sniff(filter='tcp port 80',count=10,prn=sniffer)
for i in range(10):
	a[i].show()
