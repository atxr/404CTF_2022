from pwn import *
from base64 import b64decode
import binascii

t = remote("challenge.404ctf.fr", 30117)
unknown_banned = []
banned = {'{': '', '}': '', ';': '', ':': '', "'": '', '?': '', '.': '', '>': '', ',': '', '<': '', '[': '', ']': '', '\\': '', '"': '', '|': '', '-': '', ')': '', '(': '', '*': '', '&': '', '^': '', '%': '', '$': '', '#': '', '!': '', '`': '', '~': '', '_': '', 'х': 'x', 'а': 'a', 'Т': 'T', 'е': 'e', 'о': 'o', 'у': 'y', 'р': 'p', 'К': 'K', 'Н': 'H', 'В': 'B', 'А': 'A', '@': '', 'с': 'c'}

flag=b""

j=0
while j<250:
    t.recvuntil(b"s : ")
    data = t.recvline().strip().decode()
    corr_data = ""
    for i in data:
        if i in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJLKZXCVBNM1234567890+/=":
            corr_data += i
        elif i in list(banned.keys()):
            corr_data += banned[i]
        elif i not in unknown_banned:
            unknown_banned.append(i)

    if unknown_banned != []:
        for c in unknown_banned:
            banned[c] = input(f"Unknown {c}: ").strip()

        unknown_banned = []
        j=0
        t.close()
        t = remote("challenge.404ctf.fr", 30117)
        continue

    i = 0
    while True:
        try:
            decoded = b64decode(corr_data)
        except binascii.Error:
            i += 1
            corr_data += "="
            if i>4:
                break
            continue
        break

    assert i <= 4

    b = bin(int.from_bytes(decoded, byteorder="big"))[2:]
    if len(b)%8 != 0:
        b = "0" * (-len(b) % 8) + b
    t.sendline(b.encode())

    flag += decoded

    j+=1


print("")
print("Final")
print("")

with open("flagDonneeCompromises.txt", "wb") as f:
    f.write(flag)

t.interactive()
