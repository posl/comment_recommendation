def gcd(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
N = int(input())
A = [int(i) for i in input().split()]
A.sort()
g = A[0]
for i in range(N):
    g = gcd(g, A[i])
print(g)
