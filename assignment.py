from scapy.all import *

def sniffer(packet):
	if(packet[IP].dport==80):
		print("\n{}----------HTTP--------->{}:{}:\n{}".format(packet[IP].src,packet	[IP].dst,packet[IP].dport, str(bytes(packet[TCP].payload))))
		print("Source MAC %s Dst MAC :%s"%(packet[Ether].src, packet[Ether].dst))

sniff(filter='tcp',count=10,prn=sniffer)

Output:
'''root@kali:~/ethical# python assignment.py

192.168.141.135----------HTTP--------->140.138.144.170:80:

Source MAC 00:0c:29:00:00:fa Dst MAC :00:50:56:ff:44:81

192.168.141.135----------HTTP--------->140.138.144.170:80:

Source MAC 00:0c:29:00:00:fa Dst MAC :00:50:56:ff:44:81

192.168.141.135----------HTTP--------->140.138.144.170:80:
GET /Linux/kali/pool/main/j/javatools/jarwrapper_0.64_all.deb HTTP/1.1
Host: ftp.yzu.edu.tw
User-Agent: Debian APT-HTTP/1.3 (1.6~alpha3)


Source MAC 00:0c:29:00:00:fa Dst MAC :00:50:56:ff:44:81

192.168.141.135----------HTTP--------->140.138.144.170:80:

Source MAC 00:0c:29:00:00:fa Dst MAC :00:50:56:ff:44:81

192.168.141.135----------HTTP--------->140.138.144.170:80:

Source MAC 00:0c:29:00:00:fa Dst MAC :00:50:56:ff:44:81

192.168.141.135----------HTTP--------->140.138.144.170:80:

Source MAC 00:0c:29:00:00:fa Dst MAC :00:50:56:ff:44:81'''

