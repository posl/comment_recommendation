def main():
    # 读入数据
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    # 从两个方格中的任意一个开始搜索
    # 保存到达每个方格的步数
    dist = [[-1] * W for _ in range(H)]
    # 按照广度优先搜索的顺序遍历所有方格
    que_x = []
    que_y = []
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'o':
                dist[i][j] = 0
                que_x.append(i)
                que_y.append(j)
    # 保存从两个方格中的任意一个开始搜索的结果
    res = 0
    # 保存4个方向的移动
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    while que_x:
        x = que_x.pop(0)
        y = que_y.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 判断是否可以移动
            if 0 <= nx < H and 0 <= ny < W and S[nx][ny] != '#' and dist[nx][ny] == -1:
                que_x.append(nx)
                que_y.append(ny)
                dist[nx][ny] = dist[x][y] + 1
                res = max(res, dist[nx][ny])
    print(res)

if __name__ == '__main__':
    main()