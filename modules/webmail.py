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

def check_webmail_path(url):
    login_url = f"https://{url}/webmail"
    
def check_webmail(url, username, password):
    """Check webmail login with the given credentials."""
    logger.info(f"Checking webmail for {url} with username: {username}, password: {password}")
    login_url = f"https://{url}/cp_login.php"
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9,ms;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'DNT': '1',
        'Origin': f'https://{url}',
        'Referer': f'https://{url}/cp_login.php',
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
    data = {
        'default_event': 'login_x_',
        'e68890e58a9fe69982e688bbe3828a55524c': f'https://{url}/login',
        'e5a4b1e69597e69982e688bbe3828a55524c': f'https://{url}/login',
        'e383ade382b0e382a4e383b3e5908d': username,
        'e38391e382b9e383afe383bce38389': password,
        'submit_login.x': '59',
        'submit_login.y': '16',
    }
    try:
        response = requests.post(login_url, headers=headers, data=data, verify=False)
        response.raise_for_status()
        if response.status_code == 200:
            logger.info(f"[Webmail] - [Success!] - {login_url} - {username}|{password}")
            save_result("Results/Webmail.txt", f"[+] Webmail: {login_url}\n[+] Username: {username}\n[+] Password: {password}\n\n")
        else:
            logger.info(f"[Webmail] - [Invalid!] - {login_url} - {username}|{password}")
    except requests.exceptions.RequestException as e:
        pass