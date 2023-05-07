def main():
    # 入力
    H, W, C = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    # 答えを格納する変数
    ans = float('inf')
    # 左上から右下への移動
    for i in range(H):
        for j in range(W):
            # 右下のマスから左上のマスへの移動
            for k in range(i, H):
                for l in range(j, W):
                    # 駅を建設するマスが同じマスの場合はスキップ
                    if i == k and j == l:
                        continue
                    # 駅を建設するマスが異なるマスの場合は答えを更新
                    ans = min(ans, A[i][j]+A[k][l]+C*(abs(i-k)+abs(j-l)))
    # 出力
    print(ans)
