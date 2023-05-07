def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    c = [0] * (N + 1)
    for i in range(N):
        c[i + 1] = c[i] + (p[i] + 1) / 2
    ans = 0
    for i in range(N - K + 1):
        ans = max(ans, c[i + K] - c[i])
    print(ans)
