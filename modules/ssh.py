import requests, paramiko, os
from modules.utils import save_result, setup_logging

logger = setup_logging()

def check_ssh(url, username, password):
    """Check SSH connection with the given credentials."""
    logger.info(f"Checking SSH for {url} with username: {username}, password: {password}")
    port = 22
    command = f"sshpass -p {password} ssh -o StrictHostKeyChecking=no {username}@{url} -p {port} echo 'SSH connection established'"
    try:
        result = os.system(command)
        if result == 0:
            logger.info(f"[SSH] - [Success!] - ssh://{username}@{url}:{port}")
            save_result("Results/SSH.txt", f"[+] SSH: ssh://{username}@{url}:{port}\n")
        else:
            logger.info(f"[SSH] - [Failed!] - ssh://{username}@{url}:{port}")
    except Exception as e:
        logger.info(f"[SSH] - [Error!] - ssh://{username}@{url}:{port} - {e}")