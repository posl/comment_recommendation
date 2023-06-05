def problem191_b():
    #输入
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    #处理
    result = []
    for i in range(n):
        if a[i] != x:
            result.append(a[i])
    #输出
    for i in range(len(result)):
        if i != 0:
            print(" ", end="")
        print(result[i], end="")
    print()
