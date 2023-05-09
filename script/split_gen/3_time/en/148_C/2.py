def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a
a, b = map(int, input().split())
print(a * b // gcd(a, b))
