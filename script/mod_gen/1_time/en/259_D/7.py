def main():
    N = int(input())
    sx, sy, tx, ty = map(int, input().split())
    xyr = [list(map(int, input().split())) for _ in range(N)]
    xyr.append((sx, sy, 0))
    xyr.append((tx, ty, 0))
    N += 2
    # 2N-2頂点のグラフを作成
    # 頂点0~N-2: 円の中心
    # 頂点N-1: スタート
    # 頂点N: ゴール
    # 辺: 2頂点間の距離が2つの円の半径の和以下ならつながる
    # 始点から終点までの最短経路が存在するかを判定
    # 2頂点間の距離を求める
    dist = [[float('inf') for _ in range(2*N-1)] for _ in range(2*N-1)]
    for i in range(2*N-1):
        for j in range(2*N-1):
            if i == j:
                dist[i][j] = 0
            else:
                dist[i][j] = ((xyr[i][0]-xyr[j][0])**2 + (xyr[i][1]-xyr[j][1])**2)**0.5
    # 辺をつなぐ
    for i in range(2*N-1):
        for j in range(2*N-1):
            if i == j:
                continue
            if dist[i][j] <= xyr[i][2] + xyr[j][2]:
                dist[i][j] = 1
                dist[j][i] = 1
    # ワーシャルフロイド法で全頂点間の最短経路を求める
    for k in range(2*N-1):
        for i in range(2*N-1):
            for j in range(2*N-1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    if

if __name__ == '__main__':
    main()