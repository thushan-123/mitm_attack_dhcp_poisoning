
from scapy.all import *
import socket

from scapy.layers.l2 import Ether


def main(source_mac):
    ethernet = Ether(dst="ff:ff:ff:ff:ff:ff", src=source_mac)

