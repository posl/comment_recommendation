def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
N = int(input())
print(N * 2 // gcd(N, 2))
