def problem174_b():
    #读入数据
    N,D = map(int,input().split())
    X = []
    Y = []
    for i in range(N):
        x,y = map(int,input().split())
        X.append(x)
        Y.append(y)
    #计算距离
    distance = []
    for i in range(N):
        distance.append((X[i]**2+Y[i]**2)**(1/2))
    #判断是否在圆内
    count = 0
    for i in range(N):
        if distance[i] <= D:
            count += 1
    print(count)
