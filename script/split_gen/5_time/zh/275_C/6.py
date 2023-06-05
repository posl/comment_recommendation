def main():
    # 读入数据
    s = []
    for i in range(9):
        s.append(list(input()))
    # 求解
    ans = 0
    for i in range(9):
        for j in range(9):
            if s[i][j] == '#':
                if i + 1 < 9 and j + 1 < 9:
                    if s[i + 1][j] == '#' and s[i][j + 1] == '#' and s[i + 1][j + 1] == '#':
                        ans += 1
    # 输出结果
    print(ans)
