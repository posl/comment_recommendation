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

if __name__ == '__main__':
    main()