def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    # 累積和を計算
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    # 累積和を M で割った余りごとに個数を数える
    cnt = {}
    for v in s:
        r = v % m
        if r in cnt:
            cnt[r] += 1
        else:
            cnt[r] = 1
    # 余りが同じ個数のペアの数を数える
    ans = 0
    for v in cnt.values():
        ans += v * (v - 1) // 2
    print(ans)
