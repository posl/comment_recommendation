def main():
    #入力
    N = int(input())
    X = [0] * N
    T = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], X[i], A[i] = map(int, input().split())
    #初期化
    dp = [[0] * 5 for _ in range(N + 1)]
    #dp[i][j] = i番目のスヌークまで見て、座標jにいるときの最大値
    for i in range(N):
        for j in range(5):
            if T[i] - j < 0:
                continue
            if T[i] - j > i:
                continue
            if X[i] == j:
                dp[i + 1][j] = max(dp[i][j] + A[i], dp[i][j - 1], dp[i][j + 1])
            else:
                dp[i + 1][j] = max(dp[i][j - 1], dp[i][j + 1])
    #出力
    print(dp[N][0])
