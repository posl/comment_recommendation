def main():
    # 读入数据
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # 处理数据
    # 如果作业总天数大于假期天数，直接返回-1
    if sum(A) > N:
        print(-1)
        return
    # 如果作业总天数小于等于假期天数，输出假期天数减去作业总天数
    else:
        print(N - sum(A))
        return

if __name__ == '__main__':
    main()