Synthesizing 10/10 solutions

=======
Suggestion 1

def   main (): 
     N   =   int ( input ()) 
     A   =   list ( map ( int ,   input (). split ())) 
     MOD   =   998244353 
     ans   =   [ 0 ] * 10 
     for   i   in   range ( 10 ): 
         cnt   =   0 
         for   j   in   range ( N ): 
             if   A [ j ]   ==   i : 
                 cnt   +=   1 
         ans [ i ]   =   pow ( 2 ,   cnt ,   MOD )   -   1 
     print ( "

" . join ( map ( str ,   ans )))

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 998244353
    dp = [[0] * 10 for _ in range(n)]
    dp[0][a[0]] = 1
    for i in range(1, n):
        for j in range(10):
            dp[i][(j + a[i]) % 10] += dp[i - 1][j]
            dp[i][(j * a[i]) % 10] += dp[i - 1][j]
            dp[i][(j + a[i]) % 10] %= mod
            dp[i][(j * a[i]) % 10] %= mod
    print(*dp[-1], sep='

')

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 998244353
    ans = [0] * 10
    for i in range(10):
        ans[i] = pow(2, n-1, mod) - 1
    for i in range(n):
        ans[a[i]] -= pow(2, n-1-i, mod)
    for i in range(10):
        ans[i] %= mod
    for i in range(10):
        print(ans[i])

=======
Suggestion 4

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353
    ans = [0] * 10
    ans[A[0]] = 1
    for i in range(1, N):
        ans2 = [0] * 10
        for j in range(10):
            for k in range(10):
                ans2[(j + k) % 10] += ans[j] * ans[k]
                ans2[(j * k) % 10] += ans[j] * ans[k]
        ans = ans2
    print(*ans, sep='

')
solve()

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = [0]*10
    for i in range(10):
        ans[i] = pow(2, N-1, MOD)
    for i in range(N):
        tmp = [0]*10
        for j in range(10):
            tmp[(j+A[i])%10] += ans[j]
            tmp[(j*A[i])%10] += ans[j]
        for j in range(10):
            ans[j] = tmp[j]%MOD
    for i in range(10):
        print(ans[i])

=======
Suggestion 6

def solve(N, A):
    MOD = 998244353
    ans = [0] * 10
    for i in range(10):
        for j in range(10):
            cnt = 0
            for k in range(N):
                if k % 2 == 0:
                    if A[k] == i:
                        cnt += 1
                else:
                    if A[k] == j:
                        cnt += 1
            ans[(i * j) % 10] += pow(2, cnt - 1, MOD)
    return [a % MOD for a in ans]

N = int(input())
A = list(map(int, input().split()))
print('

'.join(map(str, solve(N, A))))

=======
Suggestion 7

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    MOD = 998244353
    ans = [0]*10
    for i in range(10):
        if i == A[0]:
            ans[i] = pow(2,N-1,MOD)
    for i in range(1,N):
        for j in range(10):
            ans[j] = (ans[j]*pow(2,MOD-2,MOD)+ans[(j-A[i])%10])%MOD
    print(*ans, sep='

')

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    # MOD = 10
    dp = [[0] * 10 for _ in range(N)]
    dp[0][A[0]] = 1

    for i in range(1, N):
        for j in range(10):
            dp[i][(j + A[i]) % 10] += dp[i - 1][j]
            dp[i][(j * A[i]) % 10] += dp[i - 1][j]
            dp[i][(j + A[i]) % 10] %= MOD
            dp[i][(j * A[i]) % 10] %= MOD

    print(*dp[N - 1], sep='
')

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    # 2^N
    two_pow_N = pow(2, N-1, MOD)
    # 10^N
    ten_pow_N = pow(10, N, MOD)
    # 10^(N-1)
    ten_pow_Nminus1 = pow(10, N-1, MOD)
    # 10^(N-2)
    ten_pow_Nminus2 = pow(10, N-2, MOD)
    # 10^(N-3)
    ten_pow_Nminus3 = pow(10, N-3, MOD)

    # 0 - 9 のそれぞれに対して、最終的な値がその数字となる場合の数を求める
    for K in range(10):
        # 10^N - 10^(N-1) * A_1
        ans = (ten_pow_N - ten_pow_Nminus1 * A[0]) % MOD
        # 10^(N-1) - 10^(N-2) * A_2
        ans = (ans - ten_pow_Nminus1 + ten_pow_Nminus2 * A[1]) % MOD
        # 10^(N-2) - 10^(N-3) * A_3
        ans = (ans - ten_pow_Nminus2 + ten_pow_Nminus3 * A[2]) % MOD
        # 10^(N-3) - 10^(N-4) * A_4
        ans = (ans - ten_pow_Nminus3 + ten_pow_Nminus2 * A[3]) % MOD
        # 10^(N-4) - 10^(N-5) * A_5
        ans = (ans - ten_pow_Nminus2 + ten_pow_Nminus1 * A[4]) % MOD
        # 10^(N-5) - 10^(N-6) * A_6
        ans = (ans - ten_pow_Nminus1 + ten_pow_N * A[5]) % MOD
        # 10^(N-6) - 10^(N-7) * A_7
        ans = (ans - ten_pow_N + ten

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353

    # dp[i][j]: i桁目まで見て、mod jでの値がkになる数
    dp = [[0] * 10 for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        for j in range(10):
            dp[i][j] = dp[i - 1][j] * 2
            dp[i][(j + A[i - 1]) % 10] += dp[i - 1][j]
            dp[i][(j * A[i - 1]) % 10] += dp[i - 1][j]
            dp[i][j] %= MOD

    for i in range(10):
        print(dp[N][i])
