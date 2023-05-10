def main():
    # 標準入力の取得
    h, w = map(int, input().split())
    g = [list(input()) for i in range(h)]
    # print(h, w)
    # print(g)
    # 初期位置
    x = 0
    y = 0
    # 位置を保存
    pos = [[0 for i in range(w)] for j in range(h)]
    # print(pos)
    # 無限ループを検出するフラグ
    flag = 0
    # 無限ループを検出するためのカウンタ
    cnt = 0
    # 操作を繰り返す
    while True:
        # 次の位置を計算
        if g[x][y] == 'U':
            if x != 0:
                x -= 1
            else:
                flag = 1
        elif g[x][y] == 'D':
            if x != h - 1:
                x += 1
            else:
                flag = 1
        elif g[x][y] == 'L':
            if y != 0:
                y -= 1
            else:
                flag = 1
        elif g[x][y] == 'R':
            if y != w - 1:
                y += 1
            else:
                flag = 1
        # print(x, y)
        # 無限ループを検出した場合
        if flag == 1:
            break
        # 現在の位置に訪れた回数をカウント
        pos[x][y] += 1
        # print(pos)
        # 2回以上訪れた場合
        if pos[x][y] >= 2:
            flag = 2
            break
        # カウンタをインクリメント
        cnt += 1
        # print(cnt)
    # 結果を出力
    if flag == 1:
        print(-1)
    elif flag == 2:
        print(x + 1, y + 1)

if __name__ == '__main__':
    main()