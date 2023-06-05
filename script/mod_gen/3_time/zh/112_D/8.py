def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b%a, a)
N, M = map(int, input().split())
max_gcd = 0
for i in range(1, int(M/N)+1):
    if M % i == 0:
        max_gcd = max(max_gcd, gcd(i, M//i))
print(max_gcd)
