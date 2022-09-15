#!/usr/bin/python3
from os import urandom

def xor(msg, key):
    return b"".join([(m ^ k).to_bytes(1, "little") for m, k in zip(msg, key)])

flag = b"<REDACTED>" # The real flag is on the server and redacted for distribution
while True:
    key = urandom(len(flag))
    while b"\x00" in key:
        key = urandom(len(flag))

    cipher = xor(flag, key)
    print(cipher.hex())

    print("Send 'again' to get another encrypted flag")
    again = input()
    if again.lower() != "again":
        break

