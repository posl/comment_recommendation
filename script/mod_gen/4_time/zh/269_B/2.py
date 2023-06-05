def solve():
    # 从标准输入读取数据.
    # 10行
    s = []
    for i in range(10):
        s.append(input())
    # 从s中找到第一个有#的行
    for i in range(10):
        if '#' in s[i]:
            # 从s中找到第一个有#的列
            for j in range(10):
                if s[i][j] == '#':
                    # 找到第一个有#的行i和列j
                    # 从s中找到最后一个有#的行
                    for k in range(9, -1, -1):
                        if '#' in s[k]:
                            # 从s中找到最后一个有#的列
                            for l in range(9, -1, -1):
                                if s[k][l] == '#':
                                    # 找到最后一个有#的行k和列l
                                    # 打印结果
                                    print(i + 1, l + 1)
                                    print(k + 1, j + 1)
                                    return

if __name__ == '__main__':
    solve()