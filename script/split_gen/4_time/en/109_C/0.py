def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
N, X = map(int, input().split())
x = list(map(int, input().split()))
x.append(X)
x.sort()
diff = []
for i in range(N):
    diff.append(x[i+1] - x[i])
ans = diff[0]
for i in range(1, N):
    ans = gcd(ans, diff[i])
print(ans)
