from scapy.all import *
pcap = rdpcap('../chall/ransomware1.pcapng')
tcp_packets_out = []
for packet in pcap:
    try:
        if packet['IP'].src == '172.17.0.1':
            tcp_packets_out.append(packet)
    except:
        pass
tcp_flags = [p['TCP'].flags.value for p in tcp_packets_out]
data = b''.join([bytes([x]) for x in tcp_flags])
open('flag1.pdf', 'wb').write(data)
