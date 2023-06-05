def main():
    # 读入数据
    N = int(input())
    # 建立一个字典，记录黑色格子的坐标
    black = {}
    for i in range(N):
        x, y = map(int, input().split())
        black[(x, y)] = True
    # 定义六个方向
    dx = [-1, -1, 0, 0, 1, 1]
    dy = [-1, 0, -1, 1, 0, 1]
    # 定义一个集合，记录已经访问过的格子
    visited = {}
    # 定义一个函数，用于深度优先搜索
    def dfs(x, y):
        # 如果已经访问过了，则返回
        if visited.get((x, y)):
            return
        # 访问格子(x, y)
        visited[(x, y)] = True
        # 深度优先搜索
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            # 如果是白色格子，则返回
            if not black.get((nx, ny)):
                continue
            # 递归地访问相邻的格子
            dfs(nx, ny)
    # 计算答案
    ans = 0
    for x, y in black.keys():
        # 如果已经访问过，则返回
        if visited.get((x, y)):
            continue
        # 如果是白色格子，则返回
        if not black.get((x, y)):
            continue
        # 递归地访问相邻的格子
        dfs(x, y)
        # 计算答案
        ans += 1
    # 输出答案
    print(ans)

if __name__ == '__main__':
    main()