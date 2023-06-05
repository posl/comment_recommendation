def main():
    # 读入数据
    s = []
    for i in range(10):
        s.append(input())
    # 检查数据
    for i in range(10):
        if len(s[i]) != 10:
            print('输入数据有误')
            return
    # 找到A,B
    A = 10
    B = 1
    for i in range(10):
        if '#' in s[i]:
            if A > i:
                A = i
            if B < i:
                B = i
    # 找到C,D
    C = 10
    D = 1
    for i in range(10):
        for j in range(10):
            if s[i][j] == '#':
                if C > j:
                    C = j
                if D < j:
                    D = j
    # 输出结果
    print(A+1, B+1)
    print(C+1, D+1)
    return

if __name__ == '__main__':
    main()