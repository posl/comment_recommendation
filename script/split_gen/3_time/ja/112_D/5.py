def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
N, M = map(int, input().split())
A = list(map(int, input().split()))
g = 0
for i in range(N):
    g = gcd(g, A[i])
print(g)
