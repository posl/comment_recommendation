def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    # 累積和
    s = [0]
    for i in range(n):
        s.append(s[i] + a[i])
    # 余りの個数を数える
    cnt = [0] * m
    for i in range(n + 1):
        cnt[s[i] % m] += 1
    # 組の数を数える
    ans = 0
    for i in range(m):
        ans += cnt[i] * (cnt[i] - 1) // 2
    print(ans)
