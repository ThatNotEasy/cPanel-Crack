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

def check_plesk(url, username, password):
    """Check Plesk login with the given credentials."""
    logger.info(f"Checking Plesk for {url} with username: {username}, password: {password}")
    login_url = f"https://{url}:8443/login_up.php"
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9,ms;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
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
    params = {'success_redirect_url': '/'}
    data = {
        'login_name': username,
        'passwd': password,
    }
    try:
        response = requests.post(login_url, headers=headers, data=data, params=params, verify=False)
        response.raise_for_status()
        if response.status_code == 200:
            logger.info(f"[Plesk] - [Success!] - {login_url} - {username}|{password}")
            save_result("Results/Plesk.txt", f"[+] Plesk: {login_url}\n[+] Username: {username}\n[+] Password: {password}\n\n")
        else:
            logger.info(f"[Plesk] - [Invalid!] - {login_url} - {username}|{password}")
    except requests.exceptions.RequestException as e:
        pass