def main():
    # 读取输入
    s = []
    for i in range(9):
        s.append(input())
    # 计算
    count = 0
    for i in range(9):
        for j in range(9):
            if s[i][j] == '#':
                if i >= 1 and j >= 1 and s[i - 1][j - 1] == '#':
                    if j >= 2 and s[i][j - 2] == '#':
                        count += 1
                    if i >= 2 and s[i - 2][j] == '#':
                        count += 1
                if i >= 1 and j <= 7 and s[i - 1][j + 1] == '#':
                    if j <= 6 and s[i][j + 2] == '#':
                        count += 1
                    if i >= 2 and s[i - 2][j] == '#':
                        count += 1
                if i <= 7 and j >= 1 and s[i + 1][j - 1] == '#':
                    if j >= 2 and s[i][j - 2] == '#':
                        count += 1
                    if i <= 6 and s[i + 2][j] == '#':
                        count += 1
                if i <= 7 and j <= 7 and s[i + 1][j + 1] == '#':
                    if j <= 6 and s[i][j + 2] == '#':
                        count += 1
                    if i <= 6 and s[i + 2][j] == '#':
                        count += 1
    # 打印输出
    print(count)

if __name__ == '__main__':
    main()