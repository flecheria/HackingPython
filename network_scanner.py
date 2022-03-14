#!/usr/bin/env python3

import scapy.all as scapy
import optparse

def scan_test(ip):
  scapy.arping(ip)

def scan(ip):
  # get the field of a specific class
  # scapy.ls(scapy.ARP())

  arp_request = scapy.ARP(pdst=ip)
  # arp_request.pdst = ip

  # arp_request.show()
  # broadcast.show()
  # arp_req_broadcast.show()

  # print(arp_request.summary())
  # print(arp_req_broadcast.summary())

  broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
  arp_req_broadcast = broadcast/arp_request
  answered, unanswered = scapy.srp(arp_req_broadcast, timeout=1)

  # print(answered.summary())
  # print(unanswered.summary())

  clients = []
  # print("IP\t\t\tMAC ADDRESSS -------------------")
  for a in answered:
    # print(a[1].show())
    # print(a[1].psrc)
    # print(a[1].hwsrc)
    # print("{}\t\t{}".format(a[1].psrc, a[1].hwsrc))
    client_dict = {"ip": a[1].psrc, "mac": a[1].hwsrc}
    clients.append(client_dict)

  return clients

def print_result(clients):
  print("IP\t\t\tMAC ADDRESSS -------------------")
  for client in clients:
    print("{}\t\t{}".format(client["ip"], client["mac"]))

def get_arguments():
  parser = optparse.OptionParser()
  parser.add_option("-t", "--target", dest="network", help="network for scanning")

  (options, arguments) = parser.parse_args()

  if not options.network:
    parser.error("you forgot to enter a value for interface")

  return options.network

if __name__ == "__main__":
  network = get_arguments()
  print(network)
  clients = scan(network)
  print_result(clients)

# python network_scanner.py -t 192.168.1.0/24
# python network_scanner.py --target 192.168.1.0/24