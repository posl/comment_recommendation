def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    x.sort()
    y = []
    for i in range(N):
        y.append(x[i + 1] - x[i])
    ans = y[0]
    for i in range(N):
        ans = gcd(ans, y[i])
    print(ans)
