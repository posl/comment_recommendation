Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    L = [0] * K
    R = [0] * K
    for i in range(K):
        L[i], R[i] = map(int, input().split())
    dp = [0] * (N + 1)
    dp[1] = 1
    dp_sum = [0] * (N + 1)
    dp_sum[1] = 1
    for i in range(2, N + 1):
        for j in range(K):
            if i - L[j] <= 0:
                continue
            if i - R[j] <= 0:
                dp[i] += dp_sum[i - L[j]]
            else:
                dp[i] += dp_sum[i - L[j]] - dp_sum[i - R[j] - 1]
            dp[i] %= 998244353
        dp_sum[i] = dp_sum[i - 1] + dp[i]
        dp_sum[i] %= 998244353
    print(dp[N])

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    MOD = 998244353
    dp = [0] * (N + 1)
    dp[1] = 1
    cum = [0] * (N + 1)
    cum[1] = 1
    for i in range(2, N + 1):
        for l, r in LR:
            dp[i] += cum[max(0, i - r - 1)] - cum[max(0, i - l)]
            dp[i] %= MOD
        cum[i] = cum[i - 1] + dp[i]

    print(dp[N])

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    mod = 998244353
    dp = [0] * (N + 1)
    dp[1] = 1
    for i in range(1, N):
        for j in range(K):
            l, r = LR[j]
            dp[i + l] = (dp[i + l] + dp[i]) % mod
            dp[i + r + 1] = (dp[i + r + 1] - dp[i]) % mod
    for i in range(1, N + 1):
        dp[i] = (dp[i] + dp[i - 1]) % mod
    print(dp[N])

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    S = []
    for i in range(K):
        L, R = map(int, input().split())
        S.append((L, R))
    dp = [0] * (N + 1)
    dp_sum = [0] * (N + 1)
    dp[1] = 1
    dp_sum[1] = 1
    for i in range(2, N + 1):
        for j in range(K):
            L, R = S[j]
            dp[i] += dp_sum[max(i - L, 0)] - dp_sum[max(i - R - 1, 0)]
            dp[i] %= 998244353
        dp_sum[i] = dp_sum[i - 1] + dp[i]
    print(dp[N])

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    LR.sort(key=lambda x: x[0])
    dp = [0] * (N + 1)
    dp[1] = 1
    for i in range(1, N):
        for l, r in LR:
            dp[i + l] += dp[i]
            dp[i + l] %= 998244353
            dp[i + r + 1] -= dp[i]
            dp[i + r + 1] %= 998244353
    print(dp[N])

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    LR.sort()
    mod = 998244353
    dp = [0] * N
    dp[0] = 1
    for i in range(N - 1):
        for j in range(K):
            if LR[j][0] + i >= N:
                break
            dp[i + LR[j][0]] += dp[i]
            if LR[j][1] + i + 1 < N:
                dp[i + LR[j][1] + 1] -= dp[i]
            dp[i + LR[j][0]] %= mod
    for i in range(1, N):
        dp[i] += dp[i - 1]
        dp[i] %= mod
    print(dp[N - 1])

=======
Suggestion 7

def   main ():
     N ,  K   =   map ( int ,  input (). split ())
     L ,  R   =   [],   []
     for   _   in   range ( K ):
         l ,  r   =   map ( int ,  input (). split ())
         L . append ( l )
         R . append ( r )

     # dp[i] = number of ways to reach Cell i
     dp   =   [ 0 ] * ( N + 1 )
     dp [ 0 ]   =   1 
     # sum_dp[i] = sum of dp[0] + dp[1] + ... + dp[i]
     sum_dp   =   [ 0 ] * ( N + 1 )
     sum_dp [ 0 ]   =   1 
     for   i   in   range ( N ):
         for   j   in   range ( K ):
             dp [ i + L [ j ]]   +=   sum_dp [ i ] - sum_dp [ max ( 0 ,  i - R [ j ])] 
             dp [ i + L [ j ]]   %=   998244353 
         sum_dp [ i + 1 ]   =   ( sum_dp [ i ] + dp [ i + 1 ]) %  998244353 
     print ( dp [ N ])

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    LR.sort(key=lambda x: (x[1], x[0]))
    dp = [0] * (N + 1)
    dp[1] = 1
    for i in range(1, N):
        for l, r in LR:
            if i - l >= 0:
                dp[i + r] += dp[i - l]
                dp[i + r] %= 998244353
    print(dp[-1])

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    LR.sort()
    mod = 998244353

    def solve(N, LR):
        dp = [0] * (N + 1)
        dp[1] = 1
        for i in range(1, N):
            for l, r in LR:
                dp[i + l] = (dp[i + l] + dp[i]) % mod
                dp[i + r + 1] = (dp[i + r + 1] - dp[i]) % mod
        return dp[N]

    print(solve(N, LR))

=======
Suggestion 10

def main():
    pass
