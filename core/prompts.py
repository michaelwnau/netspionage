# from core.updater import update
from prompt_toolkit import prompt
from core.scanner import scanner_choice

def prompt_display():  
    while 1:
        user_input = prompt("\n netspionage >> ")
        if len(user_input)==0:
            print("\n")
            continue
        try:
            choice = int(user_input)
        except ValueError:
            print("\n")
            continue

        if choice == 1:
            while 1:
                print("\n 1. Network Scanner \n 2. WiFi Scanner \n 3. Port Scanner \n 4. Host Scanner\n")
                resp = input(" SCAN INPUT >> ")
                target = input(" IP ADDRESS (Eg: 192.168.1.1/24) >> ")
                print(resp)
                break
            scanner_choice(resp, target)
            # censys_ip(ip)
            continue

        if choice == 2:
            while 1:
                print("\n 1. Choose MAC Address \n 2. Input MAC Address\n")
                resp = input(" RECON INPUT >> ")
                print(resp)
                break
            # shodan_host(ip)
            # censys_ip(ip)
            continue

        if choice == 3:
            while 1:
                print("\n 1. ARP Spoof Attack \n 2. SYN Attack\n")
                resp = input(" DETECT INPUT >> ")
                print(resp)
                break
            # shodan_host(ip)
            # censys_ip(ip)
            continue

        elif choice == 4:
            while 1:
                break
            # update()
            continue

        elif choice == 5:
            exit('\n Till next time!')

        else:
            pass

try:
    prompt_display()
except KeyboardInterrupt:
    quit('\n Till next time!')