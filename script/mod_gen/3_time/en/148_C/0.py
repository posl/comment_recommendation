def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a
A, B = map(int, input().split())
print(int(A/gcd(A, B))*B)
