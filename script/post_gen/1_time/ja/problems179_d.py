Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    L = [0] * K
    R = [0] * K
    for i in range(K):
        L[i], R[i] = map(int, input().split())
    mod = 998244353
    dp = [0] * (N + 1)
    dp[1] = 1
    dp_cumsum = [0] * (N + 1)
    dp_cumsum[1] = 1
    for i in range(2, N + 1):
        for j in range(K):
            if i - L[j] >= 1:
                dp[i] += dp_cumsum[i - L[j]] - dp_cumsum[max(i - R[j] - 1, 0)]
        dp_cumsum[i] = dp_cumsum[i - 1] + dp[i]
    print(dp[N] % mod)

=======
Suggestion 2

def main():
    # 入力
    N, K = map(int, input().split())
    L = [0] * K
    R = [0] * K
    for i in range(K):
        L[i], R[i] = map(int, input().split())
    # 出力
    print(solve(N, K, L, R))

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    LR = []
    for _ in range(K):
        l, r = map(int, input().split())
        LR.append((l, r))
    mod = 998244353
    dp = [0] * (N + 1)
    dp[0] = 1
    dp[1] = 1
    S = [0] * (N + 1)
    S[0] = 1
    S[1] = 2
    for i in range(2, N + 1):
        for l, r in LR:
            dp[i] += S[max(0, i - r)] - S[max(0, i - l)]
        S[i] = S[i - 1] + dp[i]
        dp[i] %= mod
        S[i] %= mod
    print(dp[N])

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    LR.sort()
    dp = [0] * (N + 1)
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2
    dp[4] = 3
    dp[5] = 5
    for i in range(6, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4] + dp[i - 5]
        dp[i] %= 998244353
    for l, r in LR:
        dp[l] -= dp[r + 1]
        dp[l] %= 998244353
    print(dp[1])

main()

=======
Suggestion 5

def main():
    N,K = map(int,input().split())
    L = []
    R = []
    for _ in range(K):
        l,r = map(int,input().split())
        L.append(l)
        R.append(r)
    mod = 998244353
    dp = [0] * (N+1)
    dp[1] = 1
    dp[2] = -1
    for i in range(1,N):
        dp[i+1] = (dp[i+1] + dp[i]) % mod
        for j in range(K):
            dp[i+L[j]] = (dp[i+L[j]] + dp[i]) % mod
            dp[i+R[j]+1] = (dp[i+R[j]+1] - dp[i]) % mod
    for i in range(N):
        dp[i+1] = (dp[i+1] + dp[i]) % mod
    print(dp[N])

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    LR.sort(key=lambda x: x[0])
    mod = 998244353
    dp = [0] * N
    dp[0] = 1
    s = 0
    for i in range(N):
        if i > 0:
            dp[i] = (dp[i] + s) % mod
        s = (s + dp[i]) % mod
        for l, r in LR:
            if i + l >= N:
                break
            dp[i + l] = (dp[i + l] + dp[i]) % mod
            if i + r + 1 < N:
                s = (s - dp[i + r + 1]) % mod
    print(dp[-1])

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    LR.sort(key=lambda x: x[0])
    dp = [0] * (N + 1)
    dp[0] = 1
    s = [0] * (N + 1)
    s[0] = 1
    for i in range(N):
        for l, r in LR:
            if i + l > N:
                break
            dp[i + l] += s[i] - s[max(0, i - r - 1)]
            dp[i + l] %= 998244353
        s[i + 1] = (s[i] + dp[i + 1]) % 998244353
    print(dp[N])

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    LR.sort(key=lambda x: x[1])

    dp = [0] * (N + 1)
    dp[1] = 1

    for i in range(1, N):
        for l, r in LR:
            dp[i + l] += dp[i]
            dp[i + l] %= 998244353
            if i + r + 1 <= N:
                dp[i + r + 1] -= dp[i]
                dp[i + r + 1] %= 998244353

    print(dp[N])

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]

    # dp[i] = i番目のマスにたどり着く方法の数
    dp = [0] * (N + 1)
    dp[1] = 1

    # dp[i] = dp[i-1] + ... + dp[i-LR[k][1]]
    # dp[i-LR[k][0]] = dp[i-LR[k][1]] + ... + dp[i-LR[k][1]-LR[k][1]+LR[k][0]]
    # dp[i] = dp[i-1] + ... + dp[i-LR[k][1]] - dp[i-LR[k][1]-LR[k][1]+LR[k][0]] + dp[i-LR[k][1]-LR[k][1]+LR[k][0]]
    # dp[i] = dp[i-1] + ... + dp[i-LR[k][1]] - dp[i-LR[k][1]-LR[k][1]+LR[k][0]] + dp[i-LR[k][1]-LR[k][1]+LR[k][0]]
    # dp[i] = dp[i-1] + ... + dp[i-LR[k][1]] - dp[i-LR[k][1]-LR[k][1]+LR[k][0]] + dp[i-LR[k][1]-LR[k][1]+LR[k][0]]
    # dp[i] = dp[i-1] + ... + dp[i-LR[k][1]] - dp[i-LR[k][1]-LR[k][1]+LR[k][0]] + dp[i-LR[k][1]-LR[k][1]+LR[k][0]]
    # dp[i] = dp[i-1] + ... + dp[i-LR[k][1]] - dp[i-LR[k][1]-LR[k][1]+LR[k][0]] + dp[i-LR[k][1]-LR[k][1]+LR[k][0]]
    # dp[i] = dp[i-1] + ... + dp[i-LR[k][1]] - dp[i-LR[k][1]-LR[k][1]+LR[k][0]] + dp[i-LR[k][1]-LR[k][1]+LR[k][0]]

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    L, R = zip(*[map(int, input().split()) for _ in range(K)])
    L, R = list(L), list(R)

    MOD = 998244353
    dp = [0] * (N + 1)  # dp[i] = i番目のマスにたどり着く経路の数
    dp[1] = 1
    dp_sum = [0] * (N + 1)  # dp_sum[i] = dp[1] + dp[2] + ... + dp[i]
    dp_sum[1] = 1
    for i in range(2, N + 1):
        for j in range(K):
            dp[i] += dp_sum[max(i - R[j], 0)] - dp_sum[max(i - L[j], 0)]
        dp[i] %= MOD
        dp_sum[i] = (dp_sum[i - 1] + dp[i]) % MOD

    print(dp[N])
