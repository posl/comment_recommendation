def main():
    # 入力
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    # 累積和
    s = [0]
    for i in range(N):
        s.append(s[i] + a[i])
    # 累積和の差分について、K以上の個数を求める
    ans = 0
    for i in range(N):
        for j in range(i+1, N+1):
            if s[j] - s[i] >= K:
                ans += 1
    print(ans)
