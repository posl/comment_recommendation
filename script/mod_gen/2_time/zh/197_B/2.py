def main():
    # 读取输入
    h, w, x, y = map(int, input().split())
    s = [input() for _ in range(h)]
    # 计算可见的方块数
    count = 1
    for i in range(x - 2, -1, -1):
        if s[i][y - 1] == '#':
            break
        else:
            count += 1
    for i in range(x, h):
        if s[i][y - 1] == '#':
            break
        else:
            count += 1
    for j in range(y - 2, -1, -1):
        if s[x - 1][j] == '#':
            break
        else:
            count += 1
    for j in range(y, w):
        if s[x - 1][j] == '#':
            break
        else:
            count += 1
    # 输出结果
    print(count)

if __name__ == '__main__':
    main()