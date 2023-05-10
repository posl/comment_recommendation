def main():
    H, W = map(int, input().split())
    A = [list(input()) for _ in range(H)]
    # 2次元配列の初期化
    dp = [[0] * W for _ in range(H)]
    # 配列の最後の要素から逆順にループ
    for i in range(H-1, -1, -1):
        for j in range(W-1, -1, -1):
            # 配列の最後の要素だけは別処理
            if i == H-1 and j == W-1:
                continue
            # 配列の最後の行は、右にしか移動できない
            if i == H-1:
                # 青マスなら+1, 赤マスなら-1
                dp[i][j] = dp[i][j+1] + 1 if A[i][j+1] == "+" else dp[i][j+1] - 1
            # 配列の最後の列は、下にしか移動できない
            elif j == W-1:
                # 青マスなら+1, 赤マスなら-1
                dp[i][j] = dp[i+1][j] + 1 if A[i+1][j] == "+" else dp[i+1][j] - 1
            # 配列の最後の行と列以外は、右と下のどちらかに移動する
            else:
                # 青マスなら+1, 赤マスなら-1
                dp[i][j] = max(dp[i+1][j] + 1 if A[i+1][j] == "+" else dp[i+1][j] - 1, dp[i][j+1] + 1 if A[i][j+1] == "+" else dp[i][j+1] - 1)
    # 配列の最初の要素の値で判定
    if dp[0][0] > 0:
        print("Takahashi")
    elif dp[0][0] < 0:
