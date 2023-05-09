def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    r = a % b
    return gcd(b, r)
N, M = map(int, input().split())
L = [int(i) for i in range(M//N, 0, -1) if M % i == 0]
for i in L:
    if M//i >= N:
        print(i)
        break
