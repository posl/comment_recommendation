def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)
H, N = map(int, input().split())
A = list(map(int, input().split()))
g = A[0]
for i in range(1, N):
    g = gcd(g, A[i])
