def main():
    # 读入数据
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    # 排序
    A.sort(reverse=True)
    # 计算总票数
    s = sum(A)
    # 计算最小票数
    if s >= 4 * m * A[m - 1]:
        print("是")
    else:
        print("否")

if __name__ == '__main__':
    main()