#!/usr/bin/env python3

import subprocess
import optparse

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

def mac_changer(interface, new_mac):
  # more secure
  subprocess.call(["ifconfig", interface, "down"], shell=True)
  # less secure
  subprocess.call("ifconfig {0} hw ether {1}".format(interface, new_mac), shell=True)
  subprocess.call("ifconfig {0} up".format(interface), shell=True)
  # final print of the mac address
  subprocess.call("ifconfig", shell=True)

if __name__ == "__main__":
  # get value from console
  # interface = input()
  # new_mac = input()

  # get vau from command line
  (options, arguments) = get_arguments()

  if (options.interface == None or options.interface == ""):
    print("you forgot to enter a value for interface")
    raise

  if (options.new_mac == None or options.new_mac == ""):
    print("you forgot to enter a value for MAC address")
    raise

  mac_changer(options.interface, options.new_mac)
