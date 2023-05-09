def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
N, X = map(int, input().split())
x = list(map(int, input().split()))
x.append(X)
x.sort()
x = [x[i+1] - x[i] for i in range(N)]
ans = x[0]
for i in range(1, N):
    ans = gcd(ans, x[i])
print(ans)

if __name__ == '__main__':
    gcd()