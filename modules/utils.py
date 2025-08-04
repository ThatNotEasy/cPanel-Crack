import logging
import coloredlogs
import os
import socket
from typing import Optional
from urllib.parse import urlparse

def save_result(file_path, content):
    """Save the result to a specified file."""
    with open(file_path, 'a') as f:
        f.write(content)
        
        
def setup_logging(name: str = __name__, level: int = logging.DEBUG) -> logging.Logger:
    """
    Set up logging with coloredlogs and return the logger instance.
    
    Args:
        name (str): Name for the logger.
        level (int): Logging level (default: logging.DEBUG).
    
    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Define the log format
    fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    datefmt = "%Y-%m-%d %H:%M:%S"

    # Install coloredlogs
    coloredlogs.install(level=level, logger=logger, fmt=fmt, datefmt=datefmt)

    # Optional: also log to file
    if not os.path.exists("logs"):
        os.makedirs("logs")
    file_handler = logging.FileHandler("logs/debug.log", mode='a', encoding='utf-8')
    file_handler.setFormatter(logging.Formatter(fmt, datefmt))
    logger.addHandler(file_handler)

    return logger


def get_domain_from_url(url):
    """Extract domain name from URL and ensure it starts with 'https://'."""
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'https://' + url
    parsed_uri = urlparse(url)
    domain = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)
    return domain

def ip_to_domain(ip: str) -> Optional[str]:
    logger = setup_logging()
    try:
        domain = socket.gethostbyaddr(ip)[0]
        logger.info(f"[RESOLVE] {ip} → {domain}")
        return domain
    except socket.herror:
        logger.warning(f"[RESOLVE] No PTR record for {ip}")
    except Exception as e:
        logger.error(f"[RESOLVE] Error resolving {ip}: {e}")
    return None