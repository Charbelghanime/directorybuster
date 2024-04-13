#!/usr/bin/python
'''
This tool is designed for security testing purposes to identify accessible directories or paths on a web server by attempting to access them with common directory names. 
It performs HTTP GET requests to the specified target website and checks the responses against a user-defined list of valid HTTP status codes.

Usage: python3 directorybuster.py [-h] -w [WORDLIST] [-c STATUS_CODES] [-t TIMEOUT] base_url
Created by: Charbel Ghanime

'''

import requests
import argparse
from urllib.parse import urlparse
from termcolor import cprint, colored

def display_header():
    header = """
    ___.                   __                
    \_ |__  __ __  _______/  |_  ___________ 
    | __ \|  |  \/  ___/\   __\/ __ \_  __ \\
    | \_\ \  |  /\___ \  |  | \  ___/|  | \/
    |___  /____//____  > |__|  \___  >__|   
        \/           \/            \/       
    """
    print(colored(header, color='red'))
    print("by Charbel Ghanime\n")
display_header()

def ensure_scheme(url):
    """Ensures that the URL has a scheme (e.g., http://)"""
    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        return "http://" + url
    return url

def brute_force(base_url, wordlist, status_codes, timeout):
    """Brute force enumeration of URLs using a wordlist"""
    base_url = ensure_scheme(base_url)
    if not base_url.endswith('/'):
        base_url += '/'

    for word in wordlist:
        url = base_url + word.strip()
        try: 
            response = requests.get(url, timeout=timeout)

            if response.status_code in status_codes:
                print(f"Found {url} [Status Code: {response.status_code}]")

        except requests.exceptions.Timeout:
            print(f"Timeout with {url}")
        except requests.ConnectionError:
            print(f"Failed Connection {url}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Customizable web directory brute-forcing tool")
    parser.add_argument("base_url", help="Base URL of the target website")
    parser.add_argument("-w", "--wordlist", help="Path to the wordlist file", default="/usr/share/wordlists/dirb/common.txt")
    parser.add_argument("-c", "--status-codes", help="Comma-separated list of valid status codes to test (e.g., 200,301)", type=lambda s: [int(item) for item in s.split(",")], default=[200, 301, 302, 400, 403, 500, 502])
    parser.add_argument("-t", "--timeout", help="Timeout duration for HTTP requests (in seconds)", type=float, default=1)
    args = parser.parse_args()

    with open(args.wordlist, "r") as f:
        wordlist = [line.strip() for line in f]

    brute_force(args.base_url, wordlist, args.status_codes, args.timeout)

