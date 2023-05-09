def main():
    #入力
    N,M = map(int,input().split())
    A = [int(input()) for i in range(M)]
    #dp[i] = i段目にたどり着く方法の総数
    dp = [0]*(N+1)
    dp[0] = 1
    for i in range(1,N+1):
        #壊れている床を踏んでいないか
        if i not in A:
            #1段上がるか2段上がるか
            dp[i] = dp[i-1] + dp[i-2]
            dp[i] %= 1000000007
    print(dp[N])

if __name__ == '__main__':
    main()