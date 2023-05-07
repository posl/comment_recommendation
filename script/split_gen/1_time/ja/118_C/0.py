def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a
N = int(input())
A = list(map(int, input().split()))
g = A[0]
for i in range(1, N):
    g = gcd(g, A[i])
print(g)
