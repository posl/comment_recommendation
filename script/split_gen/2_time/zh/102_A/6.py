def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
n = int(input())
print(2 * n // gcd(2, n))
