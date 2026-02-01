
from scapy.all import *
import socket

from scapy.layers.inet import IP
from scapy.layers.l2 import Ether


def dhcp_offer(source_mac):
    ethernet = Ether(dst="ff:ff:ff:ff:ff:ff", src=source_mac)
    ip = IP(src="0.0.0.0", dst="255.255.255.255")

