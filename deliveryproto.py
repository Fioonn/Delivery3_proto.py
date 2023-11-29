import netmiko
from netmiko import ConnectHandler

iosv_12 = {
    'device_type' : 'cisco_ios',
    'ip' :  '192.168.56.101',
    'username' : 'prne',
    'password' : 'cisco123!',
    'secret' : 'class123!',

}

net_connect =ConnectHandler(**iosv_12)
net_connect.enable()
output = net_connect.send_command('show ip int brief')
print(output)

config_commands = [ 'int Loop 0', 'ip addre 1.1.1.1 255.255.255.0','no sh']
output = net_connect.send_config_set(config_commands)
print(output)


config_commands2 = [ 'interface gigabitethernet2', 'ip address 192.168.66.10 255.255.255.0', 'no sh' ]
output2 = net_connect.send_config_set(config_commands)
print(output2)

config_commands3 = [ 'access-list 10 deny 192.168.10.128 0.0.0.31', 'access-list 10 permit any', 'interface ethernet 0', 'ip access-group 10 out','show access-lists']
output3 = net_connect.send_config_set(config_commands3)
print(output3)

output =net_connect.send_command('show ip int brief')
print(output)
