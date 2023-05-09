def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # Aの値が大きい順にソート
    A.sort(reverse=True)
    # dp[i] := i本のマッチ棒を使って作れる整数の最大値
    dp = [0] * (N + 1)
    # dp[0] = 0
    dp[0] = 0
    # dp[1] = 0
    dp[1] = 0
    # dp[2] = 1
    dp[2] = 1
    # dp[3] = 7
    dp[3] = 7
    # dp[4] = 4
    dp[4] = 4
    # dp[5] = 2
    dp[5] = 2
    # dp[6] = 6
    dp[6] = 6
    # dp[7] = 8
    dp[7] = 8
    # dp[8] = 10
    dp[8] = 10
    # dp[9] = 18
    dp[9] = 18
    # dp[10] = 22
    dp[10] = 22
    # dp[11] = 20
    dp[11] = 20
    # dp[12] = 28
    dp[12] = 28
    # dp[13] = 68
    dp[13] = 68
    # dp[14] = 88
    dp[14] = 88
    # dp[15] = 108
    dp[15] = 108
    # dp[16] = 188
    dp[16] = 188
    # dp[17] = 200
    dp[17] = 200
    # dp[18] = 208
    dp[18] = 208
    # dp[19] = 288
    dp[19] = 288
    # dp[20] = 688
    dp[20] = 688
    # dp[21] = 888
    dp

if __name__ == '__main__':
    main()