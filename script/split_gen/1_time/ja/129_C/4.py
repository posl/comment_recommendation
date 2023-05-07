def main():
    #入力
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(M)]
    #初期化
    dp = [0] * (N + 1)
    dp[0] = 1
    dp[1] = 1
    #壊れている床を踏まないようにしながら、最上段(N 段目)にたどりつくまでの移動方法は何通りあるでしょうか？
    for i in range(2, N + 1):
        if i in A:
            dp[i] = 0
        else:
            dp[i] = dp[i-1] + dp[i-2]
    print(dp[N] % (10 ** 9 + 7))
