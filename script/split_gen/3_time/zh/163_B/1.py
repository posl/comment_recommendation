def solve():
    #读取输入
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    #排序
    a.sort()
    #计算结果
    result = 0
    for i in range(m):
        result += a[i]
    if result > n:
        result = -1
    else:
        result = n - result
    #输出结果
    print(result)
