from netfilterqueue import *
import socket, os
# used by Proxy

class rules(object):
	captureFilterStatus = False
	def __init__(self): # test
		print("i am iptables")

	def flush(self): # restore the IPTables
		print("\niptables flushed")
		os.system("iptables --flush")

	def set(self): # set-up IPTables to recieve from a certain address
		print("iptables set")
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(("8.8.8.8", 80))
		ip_addr = s.getsockname()[0]
		os.system("iptables -I INPUT -d "+ip_addr+" -j NFQUEUE --queue-num 1")

	def enableFilter(self):
		rules.captureFilterStatus = True

	def disableFilter(self):
		rules.captureFilterStatus = False
