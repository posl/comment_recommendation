def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    p = [0] + p
    s = [0] * (N + 1)
    for i in range(1, N + 1):
        s[i] = s[i - 1] + p[i]
    ans = 0
    for i in range(K, N + 1):
        ans = max(ans, s[i] - s[i - K])
    print((ans + K) / 2)
