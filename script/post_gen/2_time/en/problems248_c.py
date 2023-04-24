Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M, K = map(int, input().split())
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        for j in range(K + 1):
            for k in range(1, M + 1):
                if j - k >= 0:
                    dp[i][j] += dp[i - 1][j - k]
    print(dp[N][K] % 998244353)

=======
Suggestion 2

def main():
    N, M, K = map(int, input().split())
    MOD = 998244353
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        for j in range(K + 1):
            for k in range(M + 1):
                if j + k <= K:
                    dp[i][j + k] += dp[i - 1][j]
                    dp[i][j + k] %= MOD
    print(dp[N][K])

=======
Suggestion 3

def main():
    N, M, K = map(int, input().split())
    mod = 998244353
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        for j in range(K + 1):
            for k in range(1, M + 1):
                if j - k >= 0:
                    dp[i][j] += dp[i - 1][j - k]
                    dp[i][j] %= mod
    print(dp[N][K])

=======
Suggestion 4

def main():
    N, M, K = map(int, input().split())
    MOD = 998244353
    dp = [[0] * (K+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(K+1):
            for k in range(1, M+1):
                if j-k >= 0:
                    dp[i][j] += dp[i-1][j-k]
                    dp[i][j] %= MOD
    print(dp[N][K])

=======
Suggestion 5

def main():
    N, M, K = map(int, input().split())
    mod = 998244353
    dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        for j in range(1, K + 1):
            for k in range(1, M + 1):
                if j - k >= 0:
                    dp[i][j] += dp[i - 1][j - k]
                    dp[i][j] %= mod
    print(dp[N][K])

=======
Suggestion 6

def main():
    N, M, K = map(int, input().split())
    mod = 998244353
    dp = [0] * (K + 1)
    dp[0] = 1
    for i in range(N):
        ndp = [0] * (K + 1)
        for j in range(K + 1):
            for k in range(M + 1):
                if j + k <= K:
                    ndp[j + k] += dp[j]
                    ndp[j + k] %= mod
        dp = ndp
    print(dp[K])

=======
Suggestion 7

def solve():
    N, M, K = map(int, input().split())
    mod = 998244353
    dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(K+1):
            for k in range(1, M+1):
                if j+k <= K:
                    dp[i][j+k] += dp[i-1][j]
                    dp[i][j+k] %= mod
    print(dp[N][K])

solve()

=======
Suggestion 8

def read_ints():
    return list(map(int, input().split()))

N, M, K = read_ints()
MOD = 998244353

=======
Suggestion 9

def   main ():

    n, m, k   =   map ( int ,   input (). split ())

    mod   =   998244353

    dp   =   [ [ [ 0   for   _   in   range ( k + 1 )]   for   _   in   range ( m + 1 )]   for   _   in   range ( n + 1 )]
    dp [ 0 ][ 0 ][ 0 ]   =   1

    for   i   in   range ( n ):
         for   j   in   range ( m ):
             for   x   in   range ( k + 1 ):
                 dp [ i + 1 ][ j + 1 ][ x ]   +=   dp [ i ][ j ][ x ]
                 dp [ i + 1 ][ j + 1 ][ x ]   %=   mod

                 if   x   +   j   +   1   <=   k :
                     dp [ i + 1 ][ j + 1 ][ x   +   j   +   1 ]   +=   dp [ i ][ j ][ x ]
                     dp [ i + 1 ][ j + 1 ][ x   +   j   +   1 ]   %=   mod

    res   =   sum ( dp [ n ][ m ])   %   mod
     print ( res )
