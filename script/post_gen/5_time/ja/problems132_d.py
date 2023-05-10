Synthesizing 10/10 solutions

=======
Suggestion 1

def combination_mod(n, r, mod):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % mod

mod = 10**9 + 7
N, K = map(int, input().split())
fact = [1, 1] #fact[n] = (n! mod p)
factinv = [1, 1] #factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1] #inv[n] = (n^(-1) mod p)
for i in range(2, N+1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod // i)) % mod)
    factinv.append((factinv[-1] * inv[-1]) % mod)

for i in range(1, K+1):
    ans = combination_mod(N-K+1, i, mod) * combination_mod(K-1, i-1, mod)
    ans %= mod
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    mod = 10**9+7
    ans = [0]*K
    for i in range(1, K+1):
        ans[i-1] = i
    for i in range(2, K+1):
        ans[i-1] += ans[i-2]
    for i in range(K, N):
        ans.append(ans[i-1]*i - ans[i-K-1]*(i-K))
    print(ans[N-1]%mod)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())

    # k個の青いボールを回収するために高橋君がちょうど i 回操作をする必要があるボールの並べ方の総数
    # 1 ≤ i ≤ K
    # 1個の青いボールを回収するために高橋君がちょうど 1 回操作をする必要があるボールの並べ方は何通りあるでしょうか。
    # 1個の青いボールを回収するために高橋君がちょうど 2 回操作をする必要があるボールの並べ方は何通りあるでしょうか。
    # 1個の青いボールを回収するために高橋君がちょうど 3 回操作をする必要があるボールの並べ方は何通りあるでしょうか。
    # 1個の青いボールを回収するために高橋君がちょうど 4 回操作をする必要があるボールの並べ方は何通りあるでしょうか。
    # 1個の青いボールを回収するために高橋君がちょうど 5 回操作をする必要があるボールの並べ方は何通りあるでしょうか。
    # 1個の青いボールを回収するために高橋君がちょうど 6 回操作をする必要があるボールの並べ方は何通りあるでしょうか。
    # 1個の青いボールを回収

=======
Suggestion 4

def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod
 
mod = 10**9+7 #出力の制限
N = 10**6  # N は必要分だけ用意する
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル
 
for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )


N,K = map(int,input().split())
for i in range(K):
    if i == 0:
        print(cmb(N-K+1,K,mod))
    else:
        print((cmb(N-K+1,K-i,mod)*cmb(K+i-1,i,mod))%mod)

=======
Suggestion 5

def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

=======
Suggestion 6

def comb(n, r, mod):
    if r > n - r:
        r = n - r
    if r == 0:
        return 1
    if r == 1:
        return n
    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]
    for p in range(2, r + 1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p - 1, r, p):
                numerator[k - offset] //= pivot
                denominator[k] //= pivot
    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result = (result * numerator[k]) % mod
    return result

N, K = map(int, input().split())
mod = 10**9 + 7
for i in range(1, K + 1):
    if N - K + 1 < i:
        print(0)
    else:
        print(comb(N - K + 1, i, mod) * comb(K - 1, i - 1, mod) % mod)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())

    # dp[i][j] := i個のボールを並べるとき、j回操作する必要があるボールの並べ方
    dp = [[0 for _ in range(N+1)] for _ in range(K+1)]
    dp[0][0] = 1

    for i in range(1, K+1):
        for j in range(N+1):
            if j >= i:
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-i]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    print(dp[K][N] % (10**9+7))

=======
Suggestion 8

def comb(n, r):
    if n < r:
        return 0
    if n == 0 or r == 0:
        return 1
    if n == r:
        return 1
    if r == 1:
        return n
    if r == 2:
        return n * (n - 1) // 2
    return comb(n - 1, r - 1) + comb(n - 1, r)

N, K = map(int, input().split())

for i in range(1, K + 1):
    if N - K + 1 < i:
        print(0)
    else:
        print(comb(N - K + 1, i) * comb(K - 1, i - 1) % (10 ** 9 + 7))

=======
Suggestion 9

def main():
    N, K = list(map(int, input().split()))
    print(N, K)
    # 青の数がK個である場合の数
    # 1回の操作で連続して並ぶ青いボールを何個でも回収することができる
    # 青の数がK個の場合の数は、
    # N個のボールの並びから、K個の青いボールを取り出した時の数
    # (N-K+1)C(K) = (N-K+1)!/K!(N-K+1-K)!
    # = (N-K+1)!/K!(N-2K+1)!
    # = (N-K+1)(N-K)(N-K-1)...(N-2K+1)/K!
    # = (N-K+1)(N-K)(N-K-1)...(N-2K+1)/K(K-1)(K-2)...1
    # = (N-K+1)(N-K)(N-K-1)...(N-2K+1)/(K(K-1)(K-2)...1)
    # = (N-K+1)(N-K)(N-K-1)...(N-2K+1)(K(K-1)(K-2)...1)^-1
    # = (N-K+1)(N-K)(N-K-1)...(N-2K+1)*(K(K-1)(K-2)...1)^-1
    # = (N-K+1)(N-K)(N-K-1)...(N-2K+1)*(K(K-1)(K-2)...1)^-1
    # = (N-K+1)(N-K)(N-K-1)...(N-2K+1)*(K(K-1)(K-2)...1)^-1
    # = (N-K+1)(N-K)(N-K-1)...(N-2K+1)*(K(K-1)(K-2)...1)^-1
    # = (N-K+1)(N-K)(N-K-1)...(N-2K+1)*(K(K-

=======
Suggestion 10

def modpow(a,n,mod):
    res = 1
    while n>0:
        if n&1:
            res = res*a%mod
        a = a*a%mod
        n = n>>1
    return res
