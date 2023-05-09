def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
N, X = map(int, input().split())
x = list(map(int, input().split()))
x.append(X)
x.sort()
x = [abs(i - X) for i in x]
x = [i for i in x if i != 0]
ans = x[0]
for i in range(1, len(x)):
    ans = gcd(ans, x[i])
print(ans)
