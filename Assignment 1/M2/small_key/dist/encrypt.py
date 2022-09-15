from constants import FLAG, KEY
from Crypto.Cipher import AES

NONCE = "0000000000"
KEY += '00000000'

cipher = AES.new(KEY.encode(), AES.MODE_CTR, nonce=NONCE.encode())
print(cipher.encrypt(FLAG.encode()).hex())
