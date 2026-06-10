from pyats.topology import loader
from pprint import pprint


testbed = loader.load("~/workplace/pyats/testbed/testbed.example.yaml")

device = testbed.devices["R1"]

device.connect(log_stdout=False)

output = device.parse("show ip interface brief")

interfaces = output["interface"]

print('''Interface Health Report
-----------------------''')

for intf_name, intf_data in interfaces.items():
    status = intf_data["status"]
    protocol = intf_data["protocol"]
    
    if status == "up" and protocol == "up":
        print(f"{intf_name}: OK")
    
    elif status == "administratively down":
        print(f"{intf_name}: SKIPPED - administratively down")

    else:
        print(f"{intf_name} ALERT - status down / protocol down")
    
device.disconnect()