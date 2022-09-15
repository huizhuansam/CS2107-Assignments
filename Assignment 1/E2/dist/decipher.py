ciphertext = b'CS2107{qtxuqwq_euwujj_gcbdq_rhjhww_ouanmfdr_hxzxmm}'

for k in range(27):
    flag = b""
    for index, character in enumerate(ciphertext):
        charcode_of_a = 0x61
        charcode_of_z = 0x7a
        if charcode_of_a <= character <= charcode_of_z:
            order_in_alphabet = character - charcode_of_a
            shifted_order = (order_in_alphabet - k - index) % 26
            new_charcode = charcode_of_a + shifted_order
            flag += chr(new_charcode).encode()
        else:
            flag += chr(character).encode()
    print(flag.decode())
    