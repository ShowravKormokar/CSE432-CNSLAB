import random

# Generate random substitution table
def get_random_table():
    sub_table = {}

    # Letters from n-z
    second_half = list("nopqrstuvwxyz")

    # Shuffle letters randomly
    random.shuffle(second_half)

    # Map a-m with shuffled n-z
    for i, ch in enumerate("abcdefghijklm"):
        sub_table[ch] = second_half[i]

    return sub_table


# Encrypt / Decrypt function
def mono_alphabetic_cipher(sub_table, text):
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

sub_table = get_random_table()

print("\nRandom Substitution Table:")
for k, v in sub_table.items():
    print(f"{k} -> {v}")

# Encrypt
encrypted = mono_alphabetic_cipher(sub_table, text)

# Decrypt
decrypted = mono_alphabetic_cipher(sub_table, encrypted)

# Output
print("\nEncrypted Text:", encrypted)
print("Decrypted Text:", decrypted)