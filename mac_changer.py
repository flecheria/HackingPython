#!/usr/bin/env python3

import subprocess
import optparse
import re

original = "08:00:27:a6:1f:86"
new =      "00:11:22:33:44:55"

def get_arguments():
  parser = optparse.OptionParser()
  parser.add_option("-i", "--interface", dest="interface", help="interface for MAC change")
  parser.add_option("-m", "--mac", dest="new_mac", help="new MAC address")

  (options, arguments) = parser.parse_args()

  if not options.interface:
    parser.error("you forgot to enter a value for interface")

  if not options.new_mac:
    parser.error("you forgot to enter a value for interface")
  
  return (options, arguments)

def get_current_mac(interface):
  ifconfig_result = subprocess.check_output(["ifconfig", interface])
  current_mac_address = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))

  if (current_mac_address):
    # print(current_mac_address.group(0))
    return current_mac_address.group(0)
  else:
    return None

def mac_changer(interface, new_mac):
  # more secure
  subprocess.call(["ifconfig", interface, "down"], shell=True)
  # less secure
  subprocess.call("ifconfig {0} hw ether {1}".format(interface, new_mac), shell=True)
  subprocess.call("ifconfig {0} up".format(interface), shell=True)
  # final print of the mac address
  subprocess.call("ifconfig", shell=True)

if __name__ == "__main__":

  (options, arguments) = get_arguments()
  current_mac_address = get_current_mac(options.interface)
  print(current_mac_address)

  # change mac address only if is different from the current mac address
  if (options.new_mac is not current_mac_address):
    mac_changer(options.interface, options.new_mac)
  else:
    print("the new MAC address is equal to the current MAC address")