# Mono Alphabetic Cipher using Hardcoded Substitution Table

def mono_alphabetic_cipher(text):
    # Hardcoded substitution table
    sub_table = {
        'a': 'q',
        'b': 'w',
        'c': 'x',
        'd': 'r',
        'e': 't',
        'f': 'y',
        'g': 'u',
        'h': 's',
        'i': 'o',
        'j': 'p',
        'k': 'n',
        'l': 'v',
        'm': 'z'
    }

    result = ""

    for letter in text:
        # Encryption
        if letter in sub_table:
            result += sub_table[letter]

        # Decryption
        else:
            for k, v in sub_table.items():
                if v == letter:
                    result += k
                    break

    return result


# Main Program
text = input("Enter text to encrypt: ").lower()

# Encrypt
encrypted = mono_alphabetic_cipher(text)

# Decrypt
decrypted = mono_alphabetic_cipher(encrypted)

# Output
print("Encrypted Text:", encrypted)
print("Decrypted Text:", decrypted)