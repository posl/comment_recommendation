def main():
    # 读取输入
    s = []
    for i in range(9):
        s.append(input())
    # 统计
    ans = 0
    for i in range(9):
        for j in range(9):
            if s[i][j] == '#':
                if i == 0 or j == 0:
                    continue
                if s[i - 1][j - 1] == '#' and s[i - 1][j] == '#' and s[i][j - 1] == '#':
                    ans += 1
    # 输出
    print(ans)
