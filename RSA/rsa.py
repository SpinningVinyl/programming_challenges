import random
import secrets
import math

def is_prime(n, k=128):
    # Miller-Rabin primality test
    # n = number to test
    # k = number of tests

    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False

    # find r and s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True

def prime_candidate(bits):
    # generate prime candidate of given bit length
    p = secrets.randbits(bits)

    # make sure that the MSB is set and the number is odd (by setting the LSB to 1)
    p |= 1 << bits - 1 | 1
    return p

def generate_prime(bits):
    # generate a random prime of given length
    p = prime_candidate(bits)
    while not is_prime(p):
        p = prime_candidate(bits)
    return p

def lcm(a, b):
    # find the least common multiple of a and b
    return abs(a * b) // math.gcd(a, b)
    
def mod_inverse(a, m):
    # find the multiplicative inverse of a modulo m
    x, y = 1, 0
    x1, y1 = 0, 1
    a1, b1 = a, m
    while b1 != 0:
        q = a1 // b1
        x, x1 = x1, x - q * x1
        y, y1 = y1, y - q * y1
        a1, b1 = b1, a1 - q * b1
    return x % m

class RSA:

    def __init__(self, bits, e=65537):
        p = generate_prime(bits // 2)
        q = generate_prime(bits // 2)
        self.n = p * q
        self.e = e
        self.d = mod_inverse(self.e, lcm(p - 1, q - 1))

    def encrypt(self, m):
        return pow(m, self.e, self.n)
    
    def decrypt(self, c):
        return pow(c, self.d, self.n)


plaintext = 12345
rsa = RSA(512)
ciphertext = rsa.encrypt(plaintext)
decrypted = rsa.decrypt(ciphertext)

print('Plaintext:', plaintext)
print('Ciphertext:', ciphertext)
print('Decrypted text:', decrypted)
