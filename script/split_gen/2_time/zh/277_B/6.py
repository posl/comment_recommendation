def solve():
    #获取输入
    n = int(input().strip())
    x = int(input().strip())
    p = list(map(int, input().strip().split()))
    #处理
    for i in range(n):
        if p[i] == x:
            print(i+1)
            break
