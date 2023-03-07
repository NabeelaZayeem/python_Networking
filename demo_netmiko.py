from netmiko import ConnectHandler
#Define the device information
device={
    'device_type':'linux',
    'ip':'192.168.149.128',#Replace with the IP address of your device
    'username':'nabila',
    'password':'83098nabeela',
}
#create a Netmiko SSH connection to the device
connection=ConnectHandler(**device)
#send the "show processes cpu" command and capture the output
cpu_output=connection.send_command('cat /proc/cpuinfo')
#send the "show memory statistic" command and capture the output
mem_output=connection.send_command('free -h')
#close the Netmiko SSH connection
connection.disconnect()
#print the CPU an dmemory output
print('CPU INFORMATION:')
print(cpu_output)
print('\nMemory Information:')
print(mem_output)
