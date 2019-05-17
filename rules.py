from netfilterqueue import *
import socket, os

class rules(object):
	captureFilterStatus = False
	def __init__(self):
		print("i am iptables")

	def flush(self):
		print("\niptables flushed")
		os.system("iptables --flush")

	def set(self):
		print("iptables set")
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(("8.8.8.8", 80))
		ip_addr = s.getsockname()[0]
		os.system("iptables -I INPUT -d "+ip_addr+" -j NFQUEUE --queue-num 1")

	def enableFilter(self):
		rules.captureFilterStatus = True
