def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # 1枚目のカードをテーブルの上に置いたときの、残ったカードの整数の総和としてあり得る最小値
    dp = [0] * M
    # 1枚目のカードをテーブルの上に置いたときの、残ったカードの整数の総和としてあり得る最小値を計算する
    dp[A[0]] = 1
    for i in range(1, N):
        dp2 = [0] * M
        for j in range(M):
            if dp[j] == 0:
                continue
            dp2[j] = 1
            dp2[(j + A[i]) % M] = 1
            dp2[(j + A[i] + 1) % M] = 1
        dp = dp2
    print(sum(dp) - 1)
