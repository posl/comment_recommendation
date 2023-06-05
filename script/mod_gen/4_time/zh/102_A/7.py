def gcd(a, b):
    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    return b
n = int(input())
print(n * 2 // gcd(n, 2))
