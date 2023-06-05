def main():
    # 读取输入
    h, w = map(int, input().split())
    g = []
    for i in range(h):
        g.append(input())
    # print(g)
    # 起点
    x = 0
    y = 0
    # 方向
    direction = g[x][y]
    # print(direction)
    # 记录是否走过
    visited = [[False for _ in range(w)] for _ in range(h)]
    # print(visited)
    # 记录走过的坐标
    path = []
    # print(path)
    # 记录是否无限循环
    infinite = False
    # 重复走
    while not visited[x][y]:
        # print(x, y)
        # print(visited)
        # print(path)
        # print(infinite)
        # print()
        # 标记走过
        visited[x][y] = True
        path.append((x, y))
        # 判断方向
        if direction == 'U':
            if x == 0:
                infinite = True
                break
            else:
                x -= 1
        elif direction == 'D':
            if x == h - 1:
                infinite = True
                break
            else:
                x += 1
        elif direction == 'L':
            if y == 0:
                infinite = True
                break
            else:
                y -= 1
        elif direction == 'R':
            if y == w - 1:
                infinite = True
                break
            else:
                y += 1
        # 判断方向
        direction = g[x][y]
    # 判断是否无限循环
    if infinite:
        print(-1)
    else:
        print(x + 1, y + 1)

if __name__ == '__main__':
    main()