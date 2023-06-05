def main():
    # 输入
    n, m = map(int, input().split())
    s = []
    c = []
    for i in range(m):
        s_i, c_i = map(int, input().split())
        s.append(s_i)
        c.append(c_i)
    # 求解
    # 1. 生成所有满足条件的数字
    # 2. 从小到大排序
    # 3. 输出第一个数字
    # 4. 如果没有满足条件的数字，输出-1
    if n == 1:
        print(c[0])
    elif n == 2:
        num = []
        for i in range(10):
            for j in range(10):
                if i == c[0] and j == c[1]:
                    num.append(i * 10 + j)
        if len(num) > 0:
            num.sort()
            print(num[0])
        else:
            print(-1)
    elif n == 3:
        num = []
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    if i == c[0] and j == c[1] and k == c[2]:
                        num.append(i * 100 + j * 10 + k)
        if len(num) > 0:
            num.sort()
            print(num[0])
        else:
            print(-1)

if __name__ == '__main__':
    main()