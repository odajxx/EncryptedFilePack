'''
Forage AIG Cybersecurity Program
Bruteforce starter template
'''

from zipfile import ZipFile, BadZipFile
import sys

# Function to attempt to extract the zip file with a given password
def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password.strip())
        print(f"[+] Password found: {password.decode().strip()}")
        return True
    except (RuntimeError, BadZipFile):
        return False

def main():
    print("[+] Beginning brute-force")
    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'rb') as f:
            for line in f:
                password = line.strip()
                if attempt_extract(zf, password):
                    return  # Exit if password is found
    print("[+] Password not found in list")

if __name__ == "__main__":
    main()
