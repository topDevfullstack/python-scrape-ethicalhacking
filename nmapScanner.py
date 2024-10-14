# Nmap Scanner with Python
import subprocess
target_ip = "192.168.1.1"
nmap_command = f"nmap -p 1-1000 {target_ip}"
result = subprocess.run(nmap_command, capture_output=True, shell=True, text=True)
print("Nmap Scan Results:")
print(result.stdout)