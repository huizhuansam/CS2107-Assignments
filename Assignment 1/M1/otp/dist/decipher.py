ciphertexts = open('ciphertexts.txt', 'r')
reference_line = bytes.fromhex(ciphertexts.readline())
num_bytes = len(reference_line)

plaintext_array = [b'0' for _ in range(num_bytes)]
possible_bytes = [{i.to_bytes(1, 'little') for i in range(256)} for _ in range(num_bytes)]
remaining_bytes = num_bytes

for ciphertext in ciphertexts:
    ciphertext_bytes = bytes.fromhex(ciphertext)
    for index, ciphertext_byte in enumerate(ciphertext_bytes):
        if len(possible_bytes[index]) < 1:
            continue
        possible_bytes[index].discard(ciphertext_byte.to_bytes(1, 'little'))
        if len(possible_bytes[index]) == 1:
            plaintext_array[index] = possible_bytes[index].pop()
            remaining_bytes -= 1

    if remaining_bytes < 1:
        break

print(b''.join(plaintext_array).decode())
