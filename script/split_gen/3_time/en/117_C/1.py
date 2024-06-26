def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    d = [0] * (M - 1)
    for i in range(M - 1):
        d[i] = X[i + 1] - X[i]
    d.sort(reverse=True)
    ans = 0
    for i in range(N - 1, M - 1):
        ans += d[i]
    print(ans)
