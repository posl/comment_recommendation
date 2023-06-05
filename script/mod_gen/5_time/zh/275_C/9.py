def main():
    # 读取输入
    s = []
    for i in range(9):
        s.append(input())
    # 计算
    count = 0
    for r in range(9):
        for c in range(9):
            if s[r][c] == '#':
                if r < 8 and c < 8 and s[r + 1][c + 1] == '#' and s[r + 1][c] == '#' and s[r][c + 1] == '#':
                    count += 1
    # 输出
    print(count)

if __name__ == '__main__':
    main()