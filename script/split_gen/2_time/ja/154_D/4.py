def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    # 累積和
    s = [0] * (N+1)
    for i in range(1, N+1):
        s[i] = s[i-1] + (p[i-1] + 1) / 2
    # 最大値
    ans = 0
    for i in range(N-K+1):
        ans = max(ans, s[i+K] - s[i])
    print(ans)
