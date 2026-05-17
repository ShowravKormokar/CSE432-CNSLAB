import random
from math import gcd, isqrt


# Check if a number is prime
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False

    return True


# Generate RSA public and private keys
def generate_keypair():

    # Generate prime numbers between 50 and 200
    primes = [p for p in range(50, 200) if is_prime(p)]

    # Choose two different prime numbers
    p = random.choice(primes)
    q = random.choice(primes)

    while p == q:
        q = random.choice(primes)

    # Calculate n and phi
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose public exponent e
    e = 65537

    while gcd(e, phi) != 1:
        e = random.randint(3, phi - 1)

    # Calculate private exponent d
    d = pow(e, -1, phi)

    return (e, n), (d, n), p, q


# Encrypt integer message
def rsa_encrypt(message, public_key):
    e, n = public_key
    return pow(message, e, n)


# Decrypt integer message
def rsa_decrypt(ciphertext, private_key):
    d, n = private_key
    return pow(ciphertext, d, n)


# Convert string to ASCII values
def string_to_ascii(text):
    return [ord(char) for char in text]


# Convert ASCII values back to string
def ascii_to_string(ascii_list):
    return ''.join(chr(num) for num in ascii_list)


# Main Program
def main():

    # Generate RSA keys
    public_key, private_key, p, q = generate_keypair()

    e, n = public_key
    d, _ = private_key

    print("RSA Key Generation: ")
    print(f"Prime p           : {p}")
    print(f"Prime q           : {q}")
    print(f"n = p × q         : {n}")
    print(f"Public Key (e, n) : ({e}, {n})")
    print(f"Private Key(d, n) : ({d}, {n})")

    # Integer Encryption Example
    integer_message = 42

    encrypted_int = rsa_encrypt(integer_message, public_key)
    decrypted_int = rsa_decrypt(encrypted_int, private_key)

    print("\nInteger Encryption Example: ")
    print(f"Original Integer : {integer_message}")
    print(f"Encrypted Integer: {encrypted_int}")
    print(f"Decrypted Integer: {decrypted_int}")
    print(f"Success           : {integer_message == decrypted_int}")

    # String Encryption Example
    string_message = "HELLO"

    ascii_values = string_to_ascii(string_message)

    encrypted_text = [
        rsa_encrypt(value, public_key)
        for value in ascii_values
    ]

    decrypted_values = [
        rsa_decrypt(value, private_key)
        for value in encrypted_text
    ]

    decrypted_string = ascii_to_string(decrypted_values)

    print("\nString Encryption Example: ")
    print(f"Original String : {string_message}")
    print(f"ASCII Values    : {ascii_values}")
    print(f"Encrypted Values: {encrypted_text}")
    print(f"Decrypted String: {decrypted_string}")
    print(f"Success         : {string_message == decrypted_string}")


# Run Program
if __name__ == "__main__":
    main()