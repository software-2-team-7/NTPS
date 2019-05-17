#! /usr/bin/env python3
from kamene.all import *
from netfilterqueue import NetfilterQueue
from HookFunction.Hook import Hook
from HookFunction.HookCollection import HookCollection
from rules import rules as rules
from threading import Thread
from time import sleep
import threading


class Proxy(object):
	proxyStatus = False;
	nfqueue = NetfilterQueue()
	manager = ""
	def __init__(self):
		print("Proxy")
		self.proxyStatus = False;
		self.rule = rules()
		super().__init__()

	def modify(self, packet):
		if False:
			#testHook = Hook("Test",True,"Neat!",2,"testHook.py")
			#hooks = []
			#hc = self.manager.getCollections()
			#hc.addHook(testHook)
			newpkt = manager.executeHookSequence(packet)

		pkt = IP(packet.get_payload()) #converts the raw packet to a scapy compatible string

		#pkt.show2()

		

		packet.accept() #accept the packet

		


	def intercept(self, function):
		print("running")
		#while(self.proxyStatus):
		#rule.enableFilter() To enable filter
		#self.nfqueue = NetfilterQueue()
		self.nfqueue.unbind()
		self.nfqueue.bind(1, function)

		print ("[*] waiting for data")
		self.nfqueue.run()



	def turnOn(self):
		self.rule.set()
		self.proxyStatus = True

	def turnOff(self):	
		self.rule.flush()
		self.proxyStatus = False

	def setManager(self, manager):
		self.manager = manager

		

