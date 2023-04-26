Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    L = []
    R = []
    for i in range(K):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    
    # dp[i] = マスiにたどり着く方法の総数
    dp = [0] * (N+1)

    # dp[0] = 1
    dp[0] = 1

    # dp[i] = dp[i-1] + dp[i-2] + ... + dp[i-k] (i-k >= 0) + ... + dp[i-r] (i-r >= 0)
    # dp[i] = dp[i-1] + dp[i-2] + ... + dp[i-k] (i-k >= 0) + ... + dp[i-l] (i-l >= 0)
    for i in range(1, N+1):
        for j in range(K):
            l = i - L[j]
            r = i - R[j]
            if r < 0:
                r = 0
            if l < 0:
                l = 0
            dp[i] += dp[r] - dp[l-1]

        dp[i] = dp[i] % 998244353

    print(dp[N])

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    L = [0] * K
    R = [0] * K
    for i in range(K):
        L[i], R[i] = map(int, input().split())
    mod = 998244353
    dp = [0] * (N + 1)
    dp[1] = 1
    for i in range(2, N + 1):
        for j in range(K):
            l = max(0, i - R[j])
            r = max(0, i - L[j] + 1)
            dp[i] += dp[l] - dp[r]
        dp[i] %= mod
    print(dp[N])

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    L = []
    R = []
    for _ in range(K):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    dp = [0] * (N + 1)
    dp[1] = 1
    for i in range(1, N + 1):
        for j in range(K):
            if i + L[j] <= N:
                dp[i + L[j]] += dp[i]
                dp[i + L[j]] %= 998244353
            if i + R[j] + 1 <= N:
                dp[i + R[j] + 1] -= dp[i]
                dp[i + R[j] + 1] %= 998244353
    print(dp[N])

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    l = []
    r = []
    for i in range(k):
        li, ri = map(int, input().split())
        l.append(li)
        r.append(ri)
    #print(n, k, l, r)
    mod = 998244353
    dp = [0] * (n+1)
    dp[1] = 1
    dpsum = [0] * (n+1)
    dpsum[1] = 1
    for i in range(2, n+1):
        for j in range(k):
            li = i - r[j]
            ri = i - l[j]
            if ri < 0:
                continue
            li = max(li, 1)
            dp[i] += dpsum[ri] - dpsum[li-1]
            dp[i] %= mod
        dpsum[i] = dpsum[i-1] + dp[i]
        dpsum[i] %= mod
    #print(dp)
    print(dp[n])

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    MOD = 998244353
    dp = [0] * (N + 1)
    dp[1] = 1
    for i in range(1, N + 1):
        for l, r in LR:
            if i + l <= N:
                dp[i + l] += dp[i]
                dp[i + l] %= MOD
            if i + r + 1 <= N:
                dp[i + r + 1] -= dp[i]
                dp[i + r + 1] %= MOD
        dp[i] += dp[i - 1]
        dp[i] %= MOD
    print(dp[N])

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    mod = 998244353
    dp = [0] * (N+1)
    dp[1] = 1
    for i in range(1, N+1):
        for l, r in LR:
            if i+l <= N:
                dp[i+l] += dp[i]
                dp[i+l] %= mod
            if i+r+1 <= N:
                dp[i+r+1] -= dp[i]
                dp[i+r+1] %= mod
        dp[i] += dp[i-1]
        dp[i] %= mod
    print(dp[N])

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    lr = [list(map(int, input().split())) for _ in range(k)]
    mod = 998244353
    dp = [0]*(n+1)
    dp[1] = 1
    s = [0]*(n+1)
    s[1] = 1
    for i in range(2, n+1):
        for l, r in lr:
            if i-l < 0:
                continue
            if i-r-1 >= 0:
                dp[i] += s[i-l]-s[i-r-1]
            else:
                dp[i] += s[i-l]
        dp[i] %= mod
        s[i] = s[i-1]+dp[i]
    print(dp[n])

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    LRs = [list(map(int, input().split())) for _ in range(K)]
    mod = 998244353
    dp = [0] * N
    dp[0] = 1
    for i in range(1, N):
        for l, r in LR:
            if i - l < 0:
                continue
            dp[i] += dp[i-l] % mod
            dp[i] -= dp[max(0, i-r-1)] % mod
        dp[i] %= mod
    print(dp[-1])

=======
Suggestion 9

def main():
    # 標準入力の取得
    n, k = map(int, input().split())
    lr = [list(map(int, input().split())) for _ in range(k)]

    # 区間の和集合Sの作成
    s = set()
    for i in range(k):
        s = s | set(range(lr[i][0], lr[i][1]+1))

    # 高橋くんがマス 1 からマス N に行く方法の個数を 998244353 で割った余りを出力
    # dp[i]をiマス目にたどり着くまでの方法の数とすると、
    # dp[i] = sum(dp[i-d]) (d in S)となる。
    # dp[0] = 1とする。
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1, n+1):
        for d in s:
            if i-d >= 0:
                dp[i] += dp[i-d]
                dp[i] %= 998244353
    
    print(dp[n])

=======
Suggestion 10

def main():
    pass
