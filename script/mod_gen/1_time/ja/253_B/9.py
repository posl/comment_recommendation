def main():
    # H行W列
    H, W = map(int, input().split())
    # H行W列のマス目を表す文字列
    S = [input() for _ in range(H)]
    # 1行目のoの位置
    i = 0
    # 1行目のoの位置
    j = 0
    # 1行目のoの位置を探す
    for k in range(W):
        if S[0][k] == 'o':
            j = k
            break
    # 1行目のoの位置から下方向に探していく
    for k in range(H):
        # oが見つかったら
        if S[k][j] == 'o':
            # その位置を記録する
            i = k
    # oの位置から上方向に探していく
    for k in range(i, -1, -1):
        # oが見つからなければ
        if S[k][j] != 'o':
            # その位置から1つ下の位置を記録する
            i = k + 1
            break
    # oの位置から右方向に探していく
    for k in range(j, W):
        # oが見つからなければ
        if S[i][k] != 'o':
            # その位置から1つ左の位置を記録する
            j = k - 1
            break
    # oの位置から左方向に探していく
    for k in range(j, -1, -1):
        # oが見つからなければ
        if S[i][k] != 'o':
            # その位置から1つ右の位置を記録する
            j = k + 1
            break
    # 答えを出力する
    print(i + j)

if __name__ == '__main__':
    main()