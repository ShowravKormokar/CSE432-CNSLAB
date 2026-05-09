import random

def lehmann_primality_test(p, t=10):
    # Handle small numbers
    if p <= 2:
        return p == 2

    # Even numbers greater than 2 are composite
    if p % 2 == 0:
        return False

    # Lehmann Primality Test
    for _ in range(t):
        a = random.randint(2, p - 1)
        e = (p - 1) // 2
        res = pow(a, e, p)

        if res != 1 and res != p - 1:
            return False

    return True


# Input
num = int(input("Enter number to test for primality: "))

# Output
if lehmann_primality_test(num):
    print(f"{num}: Probably Prime")
else:
    print(f"{num}: Probably Composite")