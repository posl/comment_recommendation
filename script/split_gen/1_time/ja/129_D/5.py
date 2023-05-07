def main():
    # H,Wの読み込み
    H, W = map(int, input().split())
    # Sの読み込み
    S = [input() for _ in range(H)]
    # マスの状態を表す2次元配列
    # 0:障害物 1:通路
    masu = [[0] * W for _ in range(H)]
    # 障害物を1に変換
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                masu[i][j] = 1
    # 上から下に向かって、障害物の数をカウント
    for i in range(H):
        for j in range(W):
            if i > 0:
                masu[i][j] += masu[i-1][j]
    # 下から上に向かって、障害物の数をカウント
    for i in range(H-1, -1, -1):
        for j in range(W):
            if i < H-1:
                masu[i][j] += masu[i+1][j]
    # 左から右に向かって、障害物の数をカウント
    for i in range(H):
        for j in range(W):
            if j > 0:
                masu[i][j] += masu[i][j-1]
    # 右から左に向かって、障害物の数をカウント
    for i in range(H):
        for j in range(W-1, -1, -1):
            if j < W-1:
                masu[i][j] += masu[i][j+1]
    # 障害物の数が最小のマスを探す
    ans = 0
    for i in range(H):
        for j in range(W):
            if masu[i][j] < ans:
                ans = masu[i][j]
    # 結果を出力
    print(ans)
