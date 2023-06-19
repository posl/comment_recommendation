def main():
    #读取输入
    S = []
    for i in range(9):
        S.append(input())
    #计算结果
    result = 0
    for r in range(9):
        for c in range(9):
            if S[r][c] == '#':
                if r-1 < 0 or c-1 < 0:
                    continue
                if S[r-1][c-1] == '#' and S[r-1][c] == '#' and S[r][c-1] == '#':
                    result += 1
    #输出结果
    print(result)

if __name__ == '__main__':
    main()