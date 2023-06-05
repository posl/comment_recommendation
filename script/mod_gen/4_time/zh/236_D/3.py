def main():
    # 读取输入
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    # 用来保存最大的乐趣
    ans = 0
    # 遍历所有的可能性
    for i in range(2 ** N):
        # 用来保存当前的乐趣
        now = 0
        # 遍历所有的组合
        for j in range(N):
            for k in range(j + 1, N):
                # 如果当前的组合在i中
                if ((i >> j) & 1) == ((i >> k) & 1):
                    # 更新当前的乐趣
                    now += A[j][k]
        # 更新最大的乐趣
        ans = max(ans, now)
    # 打印答案
    print(ans)

if __name__ == '__main__':
    main()