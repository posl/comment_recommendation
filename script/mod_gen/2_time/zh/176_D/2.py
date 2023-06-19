def main():
    # 读入数据
    h, w = map(int, input().split())
    c_h, c_w = map(int, input().split())
    d_h, d_w = map(int, input().split())
    s = [input() for _ in range(h)]
    # 将坐标转化为索引
    c_h -= 1
    c_w -= 1
    d_h -= 1
    d_w -= 1
    # 将坐标转化为索引
    c_h -= 1
    c_w -= 1
    d_h -= 1
    d_w -= 1
    # 用来存储到达每个方格所需的魔法次数
    magic = [[float('inf')] * w for _ in range(h)]
    magic[c_h][c_w] = 0
    # 用来存储每个方格是否已经到达过
    visited = [[False] * w for _ in range(h)]
    # 用来存储待访问的方格
    queue = [(c_h, c_w)]
    # 朝上下左右四个方向移动
    for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nh = c_h + dh
        nw = c_w + dw
        if 0 <= nh < h and 0 <= nw < w and s[nh][nw] == '.':
            magic[nh][nw] = 0
            queue.append((nh, nw))
    # 广度优先搜索
    while queue:
        h, w = queue.pop(0)
        visited[h][w] = True
        # 朝上下左右四个方向移动
        for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nh = h + dh
            nw = w + dw
            if 0 <= nh < h and 0 <= nw < w and s[nh][nw] == '.' and not visited[nh][nw]:
                magic[nh][nw] = min(magic[nh][nw],

if __name__ == '__main__':
    main()