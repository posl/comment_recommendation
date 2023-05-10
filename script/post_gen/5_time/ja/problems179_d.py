Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    Ls = []
    Rs = []

    for i in range(K):
        L, R = map(int, input().split())
        Ls.append(L)
        Rs.append(R)

    dp = [0] * (N + 1)
    dp[1] = 1
    dpsum = [0] * (N + 1)
    dpsum[1] = 1

    for i in range(2, N + 1):
        for j in range(K):
            l = max(0, i - Rs[j])
            r = max(0, i - Ls[j] + 1)
            dp[i] += dpsum[r] - dpsum[l]
        dpsum[i] = dpsum[i - 1] + dp[i]
        dp[i] %= 998244353
        dpsum[i] %= 998244353

    print(dp[N])

=======
Suggestion 2

def main():
    # 標準入力を取得
    n, k = map(int, input().split())
    L = []
    R = []
    for i in range(k):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)

    # 計算
    # dp[i] = マスiに到達するルートの数
    # dp[i] = dp[i-1] + dp[i-2] + ... + dp[i-K]
    dp = [0] * (n+1)
    dp[1] = 1
    s = 0
    for i in range(2, n+1):
        for j in range(k):
            if i - L[j] >= 0:
                s += dp[i-L[j]]
            if i - R[j]-1 >= 0:
                s -= dp[i-R[j]-1]
        dp[i] = s % 998244353
    print(dp[n])

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    L = []
    R = []
    for i in range(K):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    MOD = 998244353
    dp = [0] * (N + 1)
    dp[1] = 1
    dpsum = [0] * (N + 1)
    dpsum[1] = 1
    for i in range(2, N + 1):
        for j in range(K):
            li = max(0, i - R[j])
            ri = max(0, i - L[j] + 1)
            dp[i] += dpsum[ri] - dpsum[li]
            dp[i] %= MOD
        dpsum[i] = dpsum[i - 1] + dp[i]
        dpsum[i] %= MOD
    print(dp[N])

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    L = [0] * K
    R = [0] * K
    for i in range(K):
        L[i], R[i] = map(int, input().split())
    MOD = 998244353
    dp = [0] * (N + 1)
    dp[1] = 1
    dpsum = [0] * (N + 1)
    dpsum[1] = 1
    for i in range(2, N + 1):
        for j in range(K):
            li = max(1, i - R[j])
            ri = max(0, i - L[j] - 1)
            dp[i] += dpsum[ri] - dpsum[li - 1]
        dp[i] %= MOD
        dpsum[i] = dpsum[i - 1] + dp[i]
    print(dp[N])

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    #print(n, k)
    #print(type(n), type(k))
    l = []
    r = []
    for i in range(k):
        li, ri = map(int, input().split())
        l.append(li)
        r.append(ri)
    #print(l, r)
    #print(type(l), type(r))
    #print(len(l), len(r))
    #print(l[0], r[0])
    #print(l[1], r[1])
    #print(l[2], r[2])
    #print(l[3], r[3])
    #print(l[4], r[4])
    #print(l[5], r[5])
    #print(l[6], r[6])
    #print(l[7], r[7])
    #print(l[8], r[8])
    #print(l[9], r[9])
    #print(l[10], r[10])
    #print(l[11], r[11])
    #print(l[12], r[12])
    #print(l[13], r[13])
    #print(l[14], r[14])
    #print(l[15], r[15])
    #print(l[16], r[16])
    #print(l[17], r[17])
    #print(l[18], r[18])
    #print(l[19], r[19])
    #print(l[20], r[20])
    #print(l[21], r[21])
    #print(l[22], r[22])
    #print(l[23], r[23])
    #print(l[24], r[24])
    #print(l[25], r[25])
    #print(l[26], r[26])
    #print(l[27], r[27])
    #print(l[28], r[28])
    #print(l[29], r[29])
    #print(l[30], r[30])
    #print(l[31], r[31])
    #print(l[32], r[32])
    #print(l[33], r[33])
    #print(l[34], r[34])
    #print(l[35], r[35])
    #print(l[36], r[36])

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    LRs = [list(map(int, input().split())) for _ in range(K)]
    MOD = 998244353

    dp = [0] * (N + 1)
    dp[1] = 1
    dpsum = [0] * (N + 1)
    dpsum[1] = 1

    for i in range(2, N + 1):
        for l, r in LR:
            li = max(0, i - r)
            ri = max(0, i - l + 1)
            dp[i] += dpsum[ri] - dpsum[li]
            dp[i] %= MOD
        dpsum[i] = dpsum[i - 1] + dp[i]
        dpsum[i] %= MOD
    print(dp[N])

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    lrs = [list(map(int, input().split())) for _ in range(k)]
    MOD = 998244353

    # dp[i]: マスiに到達する方法の数
    dp = [0] * (n+1)
    dp[1] = 1
    dpsum = [0] * (n+1)
    dpsum[1] = 1

    for i in range(2, n+1):
        for l, r in lrs:
            li = max(i-l, 1)
            ri = max(i-r-1, 0)
            dp[i] += dpsum[li] - dpsum[ri]
            dp[i] %= MOD
        dpsum[i] = dpsum[i-1] + dp[i]
        dpsum[i] %= MOD

    print(dp[n])

=======
Suggestion 8

def solve():
    N, K = map(int, input().split())
    LRs = [list(map(int, input().split())) for _ in range(K)]
    MOD = 998244353

    dp = [0] * (N + 1)
    dp[1] = 1
    dp_sum = [0] * (N + 1)
    dp_sum[1] = 1

    for i in range(2, N + 1):
        for L, R in LRs:
            l = max(1, i - R)
            r = i - L
            if r < 0:
                continue
            dp[i] += dp_sum[r] - dp_sum[l - 1]
            dp[i] %= MOD
        dp_sum[i] = dp_sum[i - 1] + dp[i]
        dp_sum[i] %= MOD

    print(dp[N])

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    L = []
    R = []
    for i in range(K):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    MOD = 998244353
    dp = [0] * (N + 1)
    dp[1] = 1
    dpsum = [0] * (N + 1)
    dpsum[1] = 1
    for i in range(2, N + 1):
        for k in range(K):
            li = max(1, i - R[k])
            ri = max(0, i - L[k] - 1)
            dp[i] += dpsum[ri] - dpsum[li - 1]
        dp[i] %= MOD
        dpsum[i] = dpsum[i - 1] + dp[i]
        dpsum[i] %= MOD
    print(dp[N])

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    mod = 998244353
    dp = [0] * (N + 1)
    dp[1] = 1
    sdp = [0] * (N + 1)
    sdp[1] = 1
    for i in range(2, N + 1):
        for l, r in LR:
            li = max(1, i - r)
            ri = max(1, i - l + 1)
            dp[i] += sdp[ri] - sdp[li - 1]
        dp[i] %= mod
        sdp[i] = sdp[i - 1] + dp[i]
        sdp[i] %= mod
    print(dp[N])
