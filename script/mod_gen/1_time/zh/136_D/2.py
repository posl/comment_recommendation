def main():
    # 读入数据
    S = input()
    N = len(S)
    # 初始化
    res = [0] * N
    for i in range(N):
        res[i] = 1
    # 模拟移动
    for i in range(10 ** 100):
        for j in range(N):
            if S[j] == 'R':
                # R向右走
                res[j + 1] += res[j]
                res[j] = 0
            else:
                # L向左走
                res[j - 1] += res[j]
                res[j] = 0
    # 输出结果
    print(' '.join(map(str, res)))

if __name__ == '__main__':
    main()