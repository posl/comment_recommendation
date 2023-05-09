def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    # 累積和
    s = [0]
    for i in range(N):
        s.append(s[-1] + (p[i] + 1) / 2)
    # 累積和の最大値
    ans = 0
    for i in range(N - K + 1):
        ans = max(ans, s[i + K] - s[i])
    print(ans)
