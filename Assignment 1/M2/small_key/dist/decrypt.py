from Crypto.Cipher import AES

ciphertext = 0x7d294f3c7a71e2808e8ce5afd9eb99c343460ca9f5f89ff062fed96b.to_bytes(28, byteorder='big')
NONCE = '0000000000'
PADDING = '00000000'

for k in range(100000000):
    num_leading_zeros = 8 - len(str(k))
    key_string = ''.join(['0' for _ in range(num_leading_zeros)]) + str(k) + PADDING
    cipher = AES.new(key_string.encode(), AES.MODE_CTR, initial_value=0, nonce=NONCE.decode())
    plaintext = cipher.decrypt(ciphertext).decode()
    try:
        print(plaintext.decode())
    except:
        continue
