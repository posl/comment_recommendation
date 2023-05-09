def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
N, M = map(int, input().split())
ans = 1
for i in range(2, min(M//N+1, M+1)):
    if M % i == 0:
        ans = max(ans, i)
        while M % i == 0:
            M //= i
