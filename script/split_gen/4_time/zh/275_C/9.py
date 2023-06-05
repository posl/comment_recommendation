def main():
    # 读入数据
    lines = []
    for i in range(9):
        lines.append(input())
    # 计算
    count = 0
    for i in range(9):
        for j in range(9):
            if lines[i][j] == '#':
                if i == 0:
                    continue
                if j == 0:
                    continue
                if lines[i - 1][j - 1] == '#':
                    if lines[i - 1][j] == '#':
                        if lines[i][j - 1] == '#':
                            count += 1
    # 输出结果
    print(count)
main()
