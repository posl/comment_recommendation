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
    for i in range(2, N + 1):
        for j in range(K):
            dp[i] += dp[max(i - R[j], 0)] - dp[max(i - L[j] - 1, 0)]
    print((dp[N] % 998244353))

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    L = [0] * K
    R = [0] * K
    for i in range(K):
        L[i], R[i] = map(int, input().split())
    #dp[i] = i番目までのセルに到達する方法の総数
    dp = [0] * (N + 1)
    dp[1] = 1
    #dp[i] = dp[i-1] + ... + dp[i-k]
    #dp[i] = dp[i-1] - dp[i-k-1] + dp[i]
    #dp[i] = 2*dp[i-1] - dp[i-k-1]
    dp2 = [0] * (N + 1)
    dp2[1] = 1
    for i in range(2, N + 1):
        dp[i] = (2 * dp[i - 1]) % 998244353
        for j in range(K):
            if i - L[j] > 0:
                dp[i] = (dp[i] - dp2[i - L[j]] + 998244353) % 998244353
        dp2[i] = (dp2[i - 1] + dp[i]) % 998244353
    print(dp[N])

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    L = [0] * K
    R = [0] * K
    for i in range(K):
        L[i], R[i] = map(int, input().split())
    dp = [0] * (N + 1)
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2
    for i in range(4, N + 1):
        for j in range(K):
            if i - L[j] >= 1:
                dp[i] += dp[i - L[j]]
            if i - R[j] >= 1:
                dp[i] -= dp[i - R[j] - 1]
    print(dp[N] % 998244353)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    L, R = [], []
    for i in range(K):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    dp = [0] * (N + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, N + 1):
        for j in range(K):
            dp[i] += dp[i - L[j]]
            dp[i] %= 998244353
            dp[i] += dp[i - R[j] - 1]
            dp[i] %= 998244353
    print(dp[N])

=======
Suggestion 5

def solve():
    N, K = map(int, input().split())
    L = [0] * K
    R = [0] * K
    for i in range(K):
        L[i], R[i] = map(int, input().split())
    dp = [0] * (N + 1)
    dp[1] = 1
    for i in range(2, N + 1):
        for j in range(K):
            dp[i] += dp[max(0, i - R[j] - 1)] - dp[max(0, i - L[j] - 1)]
        dp[i] %= 998244353
    print(dp[N])

solve()

=======
Suggestion 6

def solve():
    N, K = map(int, input().split())
    L = [0] * K
    R = [0] * K
    for i in range(K):
        L[i], R[i] = map(int, input().split())
    dp = [0] * (N + 1)
    dp[1] = 1
    sumdp = [0] * (N + 1)
    sumdp[1] = 1
    for i in range(2, N + 1):
        for j in range(K):
            l = max(1, i - R[j])
            r = max(1, i - L[j])
            dp[i] += sumdp[r] - sumdp[l - 1]
        dp[i] %= 998244353
        sumdp[i] = sumdp[i - 1] + dp[i]
    print(dp[N])

solve()

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    dp = [0] * (N+1)
    dp[1] = 1
    dp[2] = 1
    for i in range(3, N+1):
        for l, r in LR:
            dp[i] += dp[i-l] - dp[i-r-1]
    print(dp[N] % 998244353)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    mod = 998244353
    dp = [0] * (N+1)
    dp[1] = 1
    s = [0] * (N+1)
    for i in range(1, N+1):
        s[i] = s[i-1] + dp[i]
    for i in range(1, N+1):
        for l, r in LR:
            dp[i] += s[min(i+l-1, N)] - s[max(i+r-1, 0)]
            dp[i] %= mod
    print(dp[N])

=======
Suggestion 9

def   count_ways ( n ,  k ,  l ,  r ): 
     # dp[i] is the number of ways to reach cell i 
     dp   =   [ 0 ]   *   ( n   +   1 ) 
     dp [ 0 ]   =   1 
     for   i   in   range ( n ): 
         for   j   in   range ( k ): 
             if   i   +   l [ j ]   <=   n : 
                 dp [ i   +   l [ j ]]   +=   dp [ i ] 
             if   i   +   r [ j ]   +   1   <=   n : 
                 dp [ i   +   r [ j ]   +   1 ]   -=   dp [ i ] 
         dp [ i   +   1 ]   +=   dp [ i ] 
     return   dp [ n ]

=======
Suggestion 10

def dp ( n , k , l , r ): # n: N, k: K, l: L_i, r: R_i dp = [ 0 for _ in range ( n )] dp [ 0 ] = 1 for i in range ( n - 1 ): for j in range ( k ): dp [ i + l [ j ]] += dp [ i ] dp [ i + l [ j ]] %= 998244353 for j in range ( k ): dp [ i + r [ j ] + 1 ] -= dp [ i ] dp [ i + r [ j ] + 1 ] %= 998244353 return dp [ n - 1 ] n , k = map ( int , input (). split ()) l = [ 0 ] * k r = [ 0 ] * k for i in range ( k ): l [ i ], r [ i ] = map ( int , input (). split ()) print ( dp ( n , k , l , r ))
