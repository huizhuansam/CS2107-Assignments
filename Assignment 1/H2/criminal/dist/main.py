import os
import gzip
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

FLAG = b"CS2107{" + <REDACTED> + b"}"

def encrypt(plaintext):
    cipher = AES.new(os.urandom(16), AES.MODE_CTR)
    plaintext = pad(plaintext + FLAG, 16)
    plaintext = gzip.compress(plaintext)
    return cipher.encrypt(plaintext)

print("As he came into the window was a sound of a crescendo.")
print("He came into her apartment, he left the bloodstains on the carpet")
print("She ran underneath the table, he could see she was unable")
print("So she ran into the bedroom, she was struck down")
print("It was her doom\n")

print("Annie, are you okay?")
for i in range(9000):
    try:
        msg = bytes.fromhex(input("Enter a message in hex: "))
    except:
        print("Message format incorrect")
        exit(0)
    ciphertext = encrypt(msg)
    print("Ciphertext: ", ciphertext.hex())