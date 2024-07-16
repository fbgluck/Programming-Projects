# network_ping_library
# Had to install icmplib first using: "pip3 install icmplib" from PShell
# Ref: https://pypi.org/project/icmplib/
from icmplib import ping, multiping, traceroute, resolve
address = "8.8.8.8"
print(f"Pinging {address} ....")
result = ping(address, count=7, interval=1, timeout=2, id=None,
              source=None, family=None, privileged=True)
if result.is_alive:
    print(f"The system at address {result.address} is alive!")
    print(f"Packets Sent: {result.packets_sent}")
    print(f"Packets Received: {result.packets_received}")
    # RT times are returned as a list. One RT for each ping
    print("Round Trip Times:")
    for i in range(0, result.packets_sent):
        print(
            f"\tRT {i+1} - {int(result.rtts[i])*'*':<30}({result.rtts[i]:.2f})sec")
else:
    print(f"No response from {result.address}. System appears dead!")
