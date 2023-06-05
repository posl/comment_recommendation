def max_walking(h, w, maze):
    # 以(i, j)为起点的最大步数
    # 从右下角开始，递归
    def max_walking_from(i, j):
        if i == h - 1 and j == w - 1:
            return 1
        if i >= h or j >= w:
            return 0
        if maze[i][j] == '#':
            return 0
        return max(max_walking_from(i + 1, j), max_walking_from(i, j + 1)) + 1
    return max_walking_from(0, 0)

if __name__ == '__main__':
    max_walking()