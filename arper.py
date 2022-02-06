from scapy.all import
import os
import sys
import threading
import SIGNAL

interface   = "en1"
target_ip   = "192.168.1.1"
gateway_ip  = "192.168.1.254"
packet_count = 1000

# 設定要用的介面
conf.iface = interface

# 關掉輸出
conf.verb = 0

print = "[*] Setting up %s" % interface

gateway_mac =get_mac(gateway_ip)

if gateway_mac is None:
    print "[!!!] Failed to get gateway MAC. Exotomg."
    sys.exit(0)
else:
    print "[*] Gateway %s is at %s" % (gateway_ip, gateway_mac)
    target_mac = get_mac(taret_ip)
    if target_mac is None:
        print "[!!!]"
        