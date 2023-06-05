def solve():
    #读入数据
    n,s,d = map(int,input().split())
    #print(n,s,d)
    x = []
    y = []
    for i in range(n):
        x_i,y_i = map(int,input().split())
        x.append(x_i)
        y.append(y_i)
    #print(x)
    #print(y)
    #处理数据
    for i in range(n):
        if x[i] < s and y[i] > d:
            print('Yes')
            return
    print('No')
    return
solve()
