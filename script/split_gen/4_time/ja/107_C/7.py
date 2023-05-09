def main():
    from sys import stdin
    readline = stdin.readline
    N, K = map(int, readline().split())
    X = list(map(int, readline().split()))
    ans = 10 ** 18
    for i in range(N - K + 1):
        ans = min(ans, min(abs(X[i + K - 1] - X[i]) + abs(X[i]), abs(X[i + K - 1] - X[i]) + abs(X[i + K - 1])))
    print(ans)
