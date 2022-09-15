from Crypto.Random.random import randint

flag = b"<REDACTED>" # The real flag was used to generate the cipher below and redacted for distribution
assert len(flag) == 51

key = randint(1, 25)

cipher = b""
for index, character in enumerate(flag):
    charcode_of_a = 0x61
    charcode_of_z = 0x7a
    if charcode_of_a <= character <= charcode_of_z:
        order_in_alphabet = character - charcode_of_a
        shifted_order = (order_in_alphabet + key + index) % 26
        new_charcode = charcode_of_a + shifted_order
        cipher += chr(new_charcode).encode()
    else:
        cipher += chr(character).encode()

print(cipher)
# b'CS2107{qtxuqwq_euwujj_gcbdq_rhjhww_ouanmfdr_hxzxmm}'

