def main():
    # 入力
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # 累積和
    s = [0]
    for i in range(N):
        s.append(s[i] + A[i])
    # 累積和の差分について、差分がKになる組み合わせをカウント
    from collections import Counter
    c = Counter(s)
    ans = 0
    for k, v in c.items():
        ans += v * (v - 1) // 2
        if k + K in c:
            ans += v * c[k + K]
    print(ans)
