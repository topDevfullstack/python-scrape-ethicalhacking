# Simple Network Scanner
from scapy.all import ARP, Ether, srp
target_ip = "192.168.1.1/24"
arp = ARP(pdst=target_ip)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether/arp
result = srp(packet, timeout=3, verbose=0)[0]
clients = []
for sent, received in result:
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})
print("Devices on the network:")
for client in clients:
    print(f"IP: {client['ip']}\tMAC: {client['mac']}")