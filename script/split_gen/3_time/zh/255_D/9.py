def problem255_d():
    n,q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    # 1. 通过排序，找到最大值
    # 2. 通过最大值，找到最大值的下标
    # 3. 通过最大值的下标，找到最大值的最小操作数
    # 4. 通过最大值的最小操作数，计算最终的最小操作数
    # 5. 通过最终的最小操作数，计算最终的最小操作数的和
    # 1. 通过排序，找到最大值
    a.sort(reverse=True)
    # 2. 通过最大值，找到最大值的下标
    max = a[0]
    max_index = 0
    for i in range(0, n):
        if a[i] == max:
            max_index = i
    # 3. 通过最大值的下标，找到最大值的最小操作数
    max_min_op = 0
    for i in range(0, max_index):
        max_min_op += max - a[i]
    for i in range(max_index+1, n):
        max_min_op += a[i] - max
    # 4. 通过最大值的最小操作数，计算最终的最小操作数
    min_op = 0
    for i in range(0, n):
        min_op += abs(a[i] - max)
    # 5. 通过最终的最小操作数，计算最终的最小操作数的和
    sum = 0
    for i in range(0, q):
        sum += min_op - abs(a[x[i]-1] - max)
    print(sum)
