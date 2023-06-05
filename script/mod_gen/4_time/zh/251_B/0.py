def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    # print(N, W, A)
    # 1. 从小到大排序
    A.sort()
    # print(A)
    # 2. 求和
    sum_A = sum(A)
    # 3. 求最大值
    max_A = max(A)
    # 4. 求最小值
    min_A = min(A)
    # 5. 求平均值
    ave_A = sum_A / N
    # 6. 求中位数
    if N % 2 == 1:
        mid_A = A[N // 2]
    else:
        mid_A = (A[N // 2 - 1] + A[N // 2]) / 2
    # 7. 求众数
    # 众数是指一个数据序列中出现次数最多的数值
    # 众数不一定存在
    # 众数可能不止一个
    # 众数可能不��

if __name__ == '__main__':
    main()