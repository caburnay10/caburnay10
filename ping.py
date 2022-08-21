import os
from re import S
from colorama import Fore
import time
time_1 = time.time()
total_check = 0
choice = input("ENTER 'Y' for Manage Switch Full IP Scan: ")

while True:
    time.sleep(1)
    time_2 = time.time()
    if choice.upper() == 'Y':
        print(Fore.YELLOW  + "----------------------------------PING STARTED--------------------------------")
        ip_list = ['192.168.200.215', '192.168.200.217',
                   '192.168.200.202', '192.168.200.1  ',
                   '192.168.200.204', '192.168.200.205',
                   '192.168.200.211', '192.168.200.200',
                   '192.168.200.212', '192.168.200.213',
                   '192.168.200.206', '192.168.200.207',
                   '192.168.200.214', '192.168.200.208',
                   '192.168.200.105', '192.168.200.210', '192.168.200.216',
                   '192.168.200.218', '192.168.200.180',
                   '192.168.200.181', '192.168.200.182',
                   '192.168.200.183', '192.168.200.184',
                   '192.168.200.162', '192.168.200.163',
                   '192.168.200.164', '192.168.200.165',
                   '192.168.200.120', '192.168.200.121',
                   '192.168.200.122', '192.168.200.124',
                   '192.168.200.125', '192.168.200.101',
                   '192.168.200.102', '192.168.200.103',
                   '192.168.200.104','192.168.200.209']
        name = ['SERVER ROOM A13-IT OFFICE','SERVER ROOM A15-SDB LIBRARY',
                'SERVER ROOM A2 TRUNK','SERVER ROOM A3 TRUNK',
                'SERVER ROOM A4','SERVER ROOM A5-BED FACULTY',
                'SERVER ROOM A6- AVR','SERVER ROOM A1-BED 3rd Floor',
                'AVR A10-SERVER ROOM','AVR A11- REC BOOTH',
                'BED FACULTY A2- SERVER ROOM','BED FACULTY A3-BED LIBRARY',
                'BED FACULTY A12-CHAPEL CONTROL ROOM','BED LIBRARY A7- BED COMP LAB',
                'BED LIBRARY A8- BED FACULTY','BED COMPLAB A9-BED LIBRARY',
                'G7 BELTRAMI 3rd flr A14- SERVER ROOM','REGISTRAR-SERVER ROOM A16',
                'IT OFFICE B1-SERVER ROOM','IT OFFICE B2-ELEX MAIN',
                'IT OFFICE B3','IT OFFICE B4',
                'SHS COMPLAB 1','ELEX C1-IT OFFICE',
                'ELEX C2','ELEX FACULTY C3',
                'ELEX C4-TVED','TVED D1- ELEX',
                'SDB LIBRARY E1-SERVER ROOM','SDB LIBRARY E2',
                'TEAKWONDO E4','INVENTORY OFFICE E6',
                'RECORDING BOOTH F1-AVR','BOOKSTORE F2',
                'SACE F3','MACHINE SHOP G1',
                'CHAPEL CONTROL ROOM H1',]

        success_count = 0
        unsuccess_count = 0
        i = 0
        down_name = []
        for ip in ip_list:
            response = os.popen(f"ping -w 1 {ip}").read()
            if "1 received" in response:
                print(Fore.GREEN + "UP" + Fore.WHITE +
                      f"    {ip}" + Fore.GREEN + "          Ping Successful     " , end=' ')
                success_count +=1
                print(Fore.BLUE + name[i])
            else:
                print(Fore.RED + "DOWN" + Fore.WHITE +
                      f"  {ip}" + Fore.RED + "          Ping Unsuccessful   " , end=' ')
                unsuccess_count +=1
                print(Fore.BLUE + name[i])
            i += 1
        os.system('clear')
        print(Fore.YELLOW +'------------------------------------------------------------------------------')
        print(Fore.YELLOW + 'TOTAL ' + '          :  '+ Fore.GREEN +'UP = '+ str(success_count))
        print(Fore.YELLOW + 'TOTAL ' +'          :  '+ Fore.RED +'DOWN = '+ str(unsuccess_count)) 
    else:
        print(Fore.YELLOW  + "----------------------------------PING STARTED--------------------------------")
        ip_list = ['192.168.200.215',
                   '192.168.200.210', '192.168.200.120','192.168.200.121',
                   '192.168.200.125','192.168.200.209']
        name = ['SERVER ROOM A13-IT OFFICE','BED COMPLAB A9-BED LIBRARY','TVED D1- ELEX','SDB LIBRARY E2', 'INVENTORY OFFICE E6','CHAPEL CONTROL ROOM H1']
        success_count = 0
        unsuccess_count = 0
        i = 0
        down_name = []
        for ip in ip_list:
            response = os.popen(f"ping -w 1 {ip}").read()
            if "1 received" in response:
                print(Fore.GREEN + "UP" + Fore.WHITE +
                      f"    {ip}" + Fore.GREEN + "          Ping Successful     " , end=' ')
                success_count +=1
                print(Fore.BLUE + name[i])
            else:
                print(Fore.RED + "DOWN" + Fore.WHITE +
                      f"  {ip}" + Fore.RED + "          Ping Unsuccessful   " , end=' ')
                unsuccess_count +=1
                print(Fore.BLUE + name[i])
            i += 1
        os.system('clear')
        print(Fore.YELLOW +'------------------------------------------------------------------------------')
        print(Fore.YELLOW + 'TOTAL ' + '          :  '+ Fore.GREEN +'UP = '+ str(success_count))
        print(Fore.YELLOW + 'TOTAL ' +'          :  '+ Fore.RED +'DOWN = '+ str(unsuccess_count)) 
    total_check += 1
    print(Fore.YELLOW + 'CHECKING_COUNT  :  ' + Fore.GREEN + str(total_check))
    time_interval = time_2 - time_1
    minutes = time_interval//60
    hours = minutes//24
    print(Fore.YELLOW + 'UPTIME     '+ '     :  '+ Fore.GREEN + str(int(hours))+Fore.YELLOW + ' HOURS')
# import os
# ip_list = ['192.168.200.105']
# for ip in ip_list:
#     response = os.popen(f"ping -w 4 {ip}").read()
#     if "4 received" in response:
#         print(f"{ip}Ping Successful")
#     else:
#         print(f"{ip}Ping unsuccessful")