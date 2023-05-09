def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    d = [0] * (M - 1)
    for i in range(M - 1):
        d[i] = X[i + 1] - X[i]
    d.sort()
    ans = 0
    for i in range(M - N):
        ans += d[i]
    print(ans)
