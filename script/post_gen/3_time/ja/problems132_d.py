Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    mod = 10**9 + 7
    ans = [0] * (K + 1)
    for i in range(K, 0, -1):
        ans[i] = pow(K // i, N, mod)
        for j in range(2 * i, K + 1, i):
            ans[i] -= ans[j]
            ans[i] %= mod
    for i in range(1, K + 1):
        print(ans[i])

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    MOD = 10**9 + 7
    for i in range(1, K+1):
        # 青いボールをi個取る方法の数
        blue = comb(K-1, i-1)
        # 赤いボールをi個取る方法の数
        red = comb(N-K+1, i)
        print(blue * red % MOD)

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    mod = 10**9+7
    for i in range(1,k+1):
        a = n-k+1
        b = k-i
        c = i-1
        print((a*(a+b+c)//2)%mod)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    mod = 10**9+7
    # dp[i][j] := i 個のボールを j 個のグループに分けるときの分け方の数
    dp = [[0] * (N+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(1, N+1):
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j] * j) % mod
    for i in range(1, K+1):
        print(dp[N-K+1][i] * dp[K-1][i-1] % mod)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    mod = 1000000007
    for i in range(1, k+1):
        print(((k-i+1)*pow(k, mod-2, mod)*pow(k-1, i-1, mod))%mod)

=======
Suggestion 6

def main():
    N, K = list(map(int, input().split()))
    MOD = 10**9 + 7
    # dp[i][j]: i個のボールからj個の青いボールを選ぶ場合の数
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        dp[i][0] = 1
    for i in range(1, N + 1):
        for j in range(1, K + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            dp[i][j] %= MOD
    # dp2[i]: i個のボールからi個の青いボールを選ぶ場合の数
    dp2 = [0] * (N + 1)
    for i in range(1, N + 1):
        dp2[i] = dp[i][i]
    # dp3[i]: i個のボールからi個の青いボールを選ぶ場合の数の累積和
    dp3 = [0] * (N + 1)
    for i in range(1, N + 1):
        dp3[i] = (dp3[i - 1] + dp2[i]) % MOD
    # dp4[i]: i個のボールからi個の青いボールを選ぶ場合の数の累積和の累積和
    dp4 = [0] * (N + 1)
    for i in range(1, N + 1):
        dp4[i] = (dp4[i - 1] + dp3[i]) % MOD
    for i in range(1, K + 1):
        print(dp4[i])

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    MOD = 10**9+7
    # N個のうちK個を選ぶ組み合わせの数を求める
    # 1からNまでの数値があるとき、N個のうちK個を選ぶ組み合わせの数はN!/(K!*(N-K)!)となる
    # ただし、N!はNの階乗、K!はKの階乗
    # ここで、階乗を求める際は、数値の大きさによっては計算量が膨大になるため、
    # 逆元を用いて計算する
    # 逆元とは、計算機上での計算を行うための数学的な手法
    # 例えば、a*b=cとなるようなaとbがあるとき、cが求まっている場合は、
    # 逆元を用いてaを求めることができる
    # 逆元を求めるためには、フェルマーの小定理を利用する
    # フェルマーの小定理とは、
    # aとpが互いに素であるとき、aのp乗はaをpで割った余りと等しい
    # また、aの逆元はaのp-2乗と等しい
    # このことを利用して、階乗を求める際に逆元を用いることで、
    # 階乗を求める計算量を軽減できる
    # なお、逆元は、フェルマーの小定理のp-2乗の部分を計算する際に
    # べき乗の計算を行う必

=======
Suggestion 8

def main():
    N,K = map(int,input().split())
    MOD = 10**9+7
    # ボールの並べ方の総数を求める
    # 青いボールを回収する回数をiとすると、
    # 青いボールをi個回収する回数は、
    # K-i個の赤いボールを回収する回数と等しい
    # このとき、青いボールを回収する回数は、
    # N個のボールからK個のボールを選ぶ組み合わせと等しい
    # また、青いボールをi個回収する回数は、
    # N-K個のボールからi個のボールを選ぶ組み合わせと等しい
    # 以上より、青いボールをi個回収する回数は、
    # 以下の式で求められる
    # C(N,K)*C(N-K,i)
    # これをi=1,2,...,Kまで求める
    # また、C(n,k)はnCkと表記する
    # これらの和は、
    # C(N,K)*C(N-K,1)+C(N,K)*C(N-K,2)+...+C(N,K)*C(N-K,K)
    # と表せる
    # これは、
    # C(N,K)*ΣC(N-K,i)
    # と表せる
    # これを、
    # C(N,K)*ΣC(N-K,i)
    # =C(N,K)*ΣC(N-K,K-i)
    # と変形する
    # これは、
    # C(N,K)*ΣC(N-K,K-i)
    # =C(N,K)*ΣC(N-K,K-i)
    # と変形する
    # これは、
    # C(N,K)*ΣC(N-K

=======
Suggestion 9

def main():
    # 入力
    N, K = map(int, input().split())
    mod = 10**9 + 7

    # 処理
    # 青いボールを右端からi個取り除く場合の組み合わせ数
    # これを全てのiについて計算する
    # i個取り除く場合の組み合わせ数は、
    # (N-K+1)C(i) = (N-K+1)! / (i! * (N-K+1-i)!)
    # で求められる
    # ただし、i=0のときは、(N-K+1)C(0) = 1
    # それ以外のときは、(N-K+1)C(i) = (N-K+1)C(i-1) * (N-K+1-i) / i
    # となる
    # これらの値を計算する
    # また、(N-K+1)C(i)はmodで割った余りを求める
    # これは、iの最大値がKなので、
    # (N-K+1)! / (i! * (N-K+1-i)!) = (N-K+1) * (N-K+2) * ... * (N-K+1-i) / (1 * 2 * ... * i)
    # となるので、(N-K+1-i) / i のmodを求める
    # これは、pow(i, mod-2, mod)で求められる
    # これらを用いて、(N-K+1)C(i)を計算する
    # また、i=0のときは、1を代入する
    # これらの値を用いて、青いボールを右端からi個取り除く場合の組み合わせ数を計算する
    # これは、(N-K+1)C(i) * (K-1)C(i

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    MOD = 10 ** 9 + 7

    # 青いボールが連続する場合の数
    # 1個: 1通り
    # 2個: 2通り
    # 3個: 3通り
    # 4個: 5通り
    # 5個: 8通り
    # 6個: 13通り
    # 7個: 21通り
    # 8個: 34通り
    # 9個: 55通り
    # 10個: 89通り
    # 11個: 144通り
    # 12個: 233通り
    # 13個: 377通り
    # 14個: 610通り
    # 15個: 987通り
    # 16個: 1597通り
    # 17個: 2584通り
    # 18個: 4181通り
    # 19個: 6765通り
    # 20個: 10946通り
    # 21個: 17711通り
    # 22個: 28657通り
    # 23個: 46368通り
    # 24個: 75025通り
    # 25個: 121393通り
    # 26個: 196418通り
    # 27個: 317811通り
    # 28個: 514229通り
    # 29個: 832040通り
    # 30個: 1346269通り
    # 31個: 2178309通り
    # 32個: 3524578通り
    # 33個: 5702887通り
    # 34個: 9227465通り
    # 35個: 14930352通り
    # 36個: 241
