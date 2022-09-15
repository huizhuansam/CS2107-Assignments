import math
import pexpect

child = pexpect.spawn('nc cs2107-ctfd-i.comp.nus.edu.sg 5054')
prefix = 'CS2107{7his_I5_WHy_C0mpr35si0n_aR3_D!s@ble_by_d3f@ul7_'
# CS2107{7his_I5_WHy_C0mpr35si0n_aR3_D!s@ble_by_d3f@ul7_n}
plaintext = ''
prev_char = ''
postfix = ''

for i in range(7):
    child.readline()

for i in range(60):
    print('ciphertext of length ' + str(i + 1))
    min_ciphertext_len = math.inf
    candidate_char = ''
    d = {}
    for c in range(32, 127):
        # if chr(c) != prev_char:
        child.sendline((prefix + plaintext + chr(c) + postfix).encode().hex())
        child.readline()
        response = child.readline().decode()
        ciphertext = response[13:]
        d[chr(c)] = len(ciphertext)
        if len(ciphertext) <= min_ciphertext_len:
            candidate_char = chr(c)
            min_ciphertext_len = len(ciphertext)

    plaintext += candidate_char
    prev_char = candidate_char
    print(prefix + plaintext + postfix)
    print(d)

child.close()