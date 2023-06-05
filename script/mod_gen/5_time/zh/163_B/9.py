def main():
    # 读入数据
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # 计算完成作业所需的总天数
    total = sum(A)
    # 计算可以出去玩的天数
    if N >= total:
        print(N - total)
    else:
        print(-1)

if __name__ == '__main__':
    main()