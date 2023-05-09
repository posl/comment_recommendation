def main():
    N, M = map(int, input().split())
    # 初期化
    # dp[i][j]はマス(i,j)に移動するのに必要な最小操作回数
    # 初期値は-1
    dp = [[-1] * N for i in range(N)]
    # (1,1)に駒があるので初期値は0
    dp[0][0] = 0
    # マス(i,j)に駒を移動させることができるマスを全探索
    for i in range(N):
        for j in range(N):
            # 駒が移動できるマスが存在する場合
            if dp[i][j] != -1:
                # 駒が移動できるマスを全探索
                for k in range(N):
                    for l in range(N):
                        # マス(k,l)がマス(i,j)から距離がMの平方根である場合
                        if (k-i)**2 + (l-j)**2 == M:
                            # マス(k,l)に移動するのに必要な操作回数を計算
                            # マス(i,j)に駒があるのでマス(k,l)に移動するのに必要な操作回数はdp[i][j]+1
                            dp[k][l] = dp[i][j] + 1
    # 出力
    for i in range(N):
        for j in range(N):
            print(dp[i][j], end=' ')
        print()

if __name__ == '__main__':
    main()