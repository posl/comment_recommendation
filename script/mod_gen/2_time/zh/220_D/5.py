def solve():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353
    # 统计0~9出现的次数
    cnt = [0] * 10
    for a in A:
        cnt[a] += 1
    # 逆元
    inv = [0] * (N + 1)
    inv[1] = 1
    for i in range(2, N + 1):
        inv[i] = (-(mod // i) * inv[mod % i]) % mod
    # 计算阶乘
    fact = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = fact[i - 1] * i % mod
    # 计算组合数
    def comb(n, k):
        if n < k:
            return 0
        return fact[n] * inv[k] * inv[n - k] % mod
    # 计算答案
    ans = [0] * 10
    for K in range(10):
        for i in range(0, N + 1, 2):
            j = N - i
            if i > j:
                break
            if i == j:
                ans[K] += comb(cnt[K], i // 2)
            else:
                ans[K] += comb(cnt[K], i) * comb(N - cnt[K], j)
            ans[K] %= mod
    for i in range(10):
        print(ans[i])
solve()
