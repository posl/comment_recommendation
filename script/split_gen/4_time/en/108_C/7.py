def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
n,k = map(int, input().split())
