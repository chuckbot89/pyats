from pyats.topology import loader
from pprint import pprint

testbed = loader.load("~/workplace/pyats/testbed/testbed.example.yaml")
device = testbed.devices["R1"]

device.connect(log_stdout=False)
output = device.parse("show version")

version_data = output['version']['version']

# if version != '10.2(5)':
#     print("업그레이드 필요")
    
pprint(version)

device.disconnect()