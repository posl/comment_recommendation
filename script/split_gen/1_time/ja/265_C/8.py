def main():
    H, W = map(int, input().split())
    G = [input() for _ in range(H)]
    #print(H, W)
    #print(G)
    # すでに通った場所を記録する
    visited = [[False] * W for _ in range(H)]
    #print(visited)
    # 今いる場所
    i = 0
    j = 0
    # 移動回数
    cnt = 0
    # すでに通った場所かどうかを確認
    while not visited[i][j]:
        visited[i][j] = True
        cnt += 1
        #print(i, j)
        # 移動する
        if G[i][j] == 'U':
            i -= 1
        elif G[i][j] == 'D':
            i += 1
        elif G[i][j] == 'L':
            j -= 1
        elif G[i][j] == 'R':
            j += 1
        # 移動先がグリッドの範囲外ならば終了
        if i < 0 or i >= H or j < 0 or j >= W:
            break
    # 移動回数がグリッドのマス数より多ければ無限ループ
    if cnt > H * W:
        print(-1)
    else:
        print(i + 1, j + 1)
