def encrypt(plaintext, width = 4):
    length = len(plaintext)
    ciphertext = ""

    for k in range(width):
        for i in range(k, length, width):
            ciphertext += plaintext[i]

    return ciphertext

def decrypt(cipher_text, width = 4):
    length = len(cipher_text)
    plain_text = [''] * length
    idx = 0

    for k in range(width):
        for i in range(k, length, width):
            plain_text[i] = cipher_text[idx]
            idx += 1

    return ''.join(plain_text)

plaintext = "DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING, VU"
ciphertext = encrypt(plaintext)
decrypted_text = decrypt(ciphertext)
print(f"Plain text: {plaintext}")
print(f"Cipher text: {ciphertext}")
print(f"Decrypted text: {decrypted_text}")