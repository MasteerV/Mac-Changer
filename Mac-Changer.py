import os          
import getpass

def ascii_art():
    print("")
    print("        |\ |\\")
    print("        \ \| |")
    print("         \ | |")
    print("       .--''/")
    print("      /o     \\")
    print("      \      /     Mac-Changer")
    print("      {>o<}='      from MasteerV")
    print("")

def clear():
    os.system('clear')

#we make a function to run bash script that filter the result of ifconfig with only the mac address
def your_actual_mac():
    os.system('echo \'ifconfig | grep "ether" | cut -d "x" -f1 | cut -d "r" -f2 | cut -d "t" -f1\' > mac_info.sh')
    print('Actual MAC:')
    os.system('bash mac_info.sh')
    os.system('rm mac_info.sh')

#power off ethernet adapter
def ethernet_adapter_down(ethernet_adapter):
    os.system('ifconfig ' + str(ethernet_adapter) + ' down')

#change mac address for new macc address
def changing_mac(new_mac_address, ethernet_adapter):
    os.system('ifconfig ' + str(ethernet_adapter) + ' hw ether ' + str(new_mac_address))

#power on ethernet adapter
def ethernet_adapter_up(ethernet_adapter):
    os.system('ifconfig ' + str(ethernet_adapter) + ' up')

#like your_actual_mac() but with new mac address
def your_changed_mac():
    os.system('echo \'ifconfig | grep "ether" | cut -d "x" -f1 | cut -d "r" -f2 | cut -d "t" -f1\' > mac_info.sh')
    print('Actual MAC:')
    os.system('bash mac_info.sh')
    os.system('rm mac_info.sh')

#we get the username 
user_name = getpass.getuser()

#the script only run with root
if user_name == 'root':
    clear()
    ascii_art()
    your_actual_mac()

    #loop to know if ethernet adapter name is correct
    while True:
        ethernet_adapter = input('Enter ethernet adapter Ej: eth0 > > > ')
        if ('eth' in ethernet_adapter) or ('wlan' in ethernet_adapter):
            break
        else:
            print('Invalid ethernet adapter, try again.')

    new_mac_address = input('Enter new mac > > > ')

    ethernet_adapter_down(ethernet_adapter)
    changing_mac(new_mac_address, ethernet_adapter)
    ethernet_adapter_up(ethernet_adapter)
    your_changed_mac()
else:
    print('Please, try again with root')