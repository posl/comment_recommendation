def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
N, X = map(int, input().split())
x = list(map(int, input().split()))
x.append(X)
x.sort()
D = x[1] - x[0]
for i in range(1, N):
    D = gcd(D, x[i+1] - x[i])
print(D)
