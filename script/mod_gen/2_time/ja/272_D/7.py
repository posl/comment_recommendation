def main():
    N, M = map(int, input().split())
    # N = 400, M = 10**6 なので、Mの平方根の整数部分を求める
    M = int(M**0.5)
    # 2次元配列の初期化
    ans = [[-1 for _ in range(N)] for _ in range(N)]
    # 初期位置の設定
    ans[0][0] = 0
    # 1次元配列の初期化
    que = [[0, 0]]
    # Mの平方根の整数部分を超えるまで、1次元配列の要素を取り出す
    while que:
        # 1次元配列の要素を取り出す
        x, y = que.pop(0)
        # 1次元配列の要素を元に、上下左右にMの平方根の整数部分の距離を移動できるかを確認する
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nx, ny = x + dx, y + dy
            # 移動先がマス目の範囲外の場合、処理をスキップする
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            # 移動先が未訪問の場合、移動先の距離を設定する
            if ans[nx][ny] == -1:
                ans[nx][ny] = ans[x][y] + 1
                # 移動先がMの平方根の整数部分の距離である場合、移動先を1次元配列に追加する
                if ans[nx][ny] == M:
                    que.append([nx, ny])
    # 結果を出力する
    for i in range(N):
        print(*ans[i])

if __name__ == '__main__':
    main()