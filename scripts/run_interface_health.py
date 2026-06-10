from pyats.topology import loader
from scripts.interface_health import interface_health_check


testbed = loader.load("testbed/testbed.example.yaml")
device = testbed.devices["R1"]

device.connect(log_stdout=False)

output = device.parse("show ip interface brief")
results = interface_health_check(output)

print("Interface Health Report")
print("-----------------------")

for item in results:
    print(
        f'{item["interface"]}: {item["state"]} '
        f'- status {item["status"]} / protocol {item["protocol"]}'
    )

device.disconnect()