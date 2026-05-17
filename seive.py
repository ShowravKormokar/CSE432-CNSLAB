# Sieve of Eratosthenes

N = 500
prime = [0] * 1000

# inserting values into array
for i in range(0, N + 1):
    prime[i] = i

prime[0] = 0
prime[1] = 0

# sieve algorithm
i = 2

while i * i <= N:
    if prime[i] != 0:
        j = i * i
        while j <= N:
            prime[j] = 0
            j += i

    i += 1

# printing prime numbers
print("Prime Numbers are:")

for i in range(2, N + 1):
    if prime[i] != 0:
        print(prime[i], end=" ")