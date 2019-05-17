from kamene.all import *
##from Scapy.all import *

class run:
    def execute(self, packet):
        if(packet.haslayer(TCP)):
            dst = packet.dst
            src = packet.src
            srcPort = packet.sport
            dstPort = packet.dport
            seq = packet.seq
            ack = packet.ack


            ip = IP(src = src, dst = dst)
            
            SYN = TCP(sport = srcPort, dport = dstPort, flag = 'S', seq = seq, ack = ack)
            SYN_ACK = sr1(ip/SYN) #only returns one packet that answered the packet sent.

            ACK = TCP(sport = srcPort, dport = dstPort, flag = 'A', seq = SYN_ACK.ack + 1, ack = SYN_ACK.seq + 1)
            send(ip/ACK)
            

