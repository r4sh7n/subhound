#!/usr/bin/env python3
import subprocess
import requests
import dns.resolver
import time
import os

def banner():
    print(r'''
   ____        _     _                     _                 
  / ___| _   _| |__ | |__   ___  _ __   __| | ___ _ __ ___   
  \___ \| | | | '_ \| '_ \ / _ \| '_ \ / _` |/ _ \ '__/ _ \  
   ___) | |_| | |_) | |_) | (_) | | | | (_| |  __/ | | (_) | 
  |____/ \__,_|_.__/|_.__/ \___/|_| |_|\__,_|\___|_|  \___/  

           🔎 SubHound v1.0 — Hunt Subdomains Like a Hound
    ''')

# Subdomain Enumeration via Sublist3r
def sublist3r_enum(domain):
    print(f"\n[+] Running Sublist3r for {domain}...\n")
    subprocess.run(["sublist3r", "-d", domain, "-o", "subdomains.txt"])

# Wildcard domain check
def is_wildcard(domain):
    resolver = dns.resolver.Resolver()
    wildcard_detected = False
    test_subs = ['www', 'dev', 'random', 'test123']
    for sub in test_subs:
        try:
            full_domain = f"{sub}.{domain}"
            result = resolver.resolve(full_domain, 'A')
            for ip in result:
                print(f"[!] Wildcard detected: {full_domain} -> {ip}")
                wildcard_detected = True
                break
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.Timeout):
            continue
    return wildcard_detected

# DNS check on found subdomains
def check_subdomains():
    if not os.path.exists("subdomains.txt"):
        print("[-] No subdomains.txt found!")
        return

    print("\n[+] Checking for wildcard domains...\n")
    with open("subdomains.txt", "r") as f:
        subs = [x.strip() for x in f.readlines()]
    
    for sub in subs:
        print(f"[+] Checking {sub}...")
        if is_wildcard(sub):
            print(f"[!] {sub} seems to be part of a wildcard domain.\n")

# Main logic
def main():
    banner()
    domain = input("Enter target domain (e.g. example.com): ").strip()
    sublist3r_enum(domain)
    time.sleep(1)
    check_subdomains()
    print("\n[✔] Done. Results saved in subdomains.txt")

if __name__ == "__main__":
    main()
