def main():
    S = input()
    N = len(S)
    mod = 2019
    #dp[i][j] = (S[i:j] % mod)を格納する
    dp = [[0] * (N+1) for _ in range(N+1)]
    #dp[i][j] = (S[i:j] % mod)を計算する
    for i in range(N):
        for j in range(i+1, N+1):
            dp[i][j] = (dp[i][j-1] * 10 + int(S[j-1])) % mod
    #print(dp)
    #dp[i][j] = (S[i:j] % mod)の値が2019で割り切れる個数をカウントする
    #dp[i][j] = (S[i:j] % mod)の値が2019で割り切れる個数は、
    #dp[i][j] = (S[i:j] % mod)の値がmodで割った余りが0の個数
    #dp[i][j] = (S[i:j] % mod)の値がmodで割った余りが0の個数は、
    #dp[i][j] = (S[i:j] % mod)の値がmodで割った余りがmod-1の個数
    #dp[i][j] = (S[i:j] % mod)の値がmodで割った余りがmod-2の個数
    #dp[i][j] = (S[i:j] % mod)の値がmodで割った余りがmod-3の個数
    #dp[i][j] = (S[i:j] % mod)の値がmodで割った余りがmod-4の個数
    #dp[i][j] = (S[i:j] % mod)の値がmodで割った余りがmod-5の個数
    #dp[i][j] = (S[i:j] % mod)の値がmodで割った余りがmod-6

if __name__ == '__main__':
    main()