def solve():
    #N是蛋糕种类，M是要吃的蛋糕数
    N,M = map(int,input().split())
    #蛋糕的美丽度、美味度和受欢迎度
    cakes = []
    for i in range(N):
        cakes.append(list(map(int,input().split())))
    #将蛋糕按照美丽度、美味度和受欢迎度排序
    cakes = sorted(cakes, key=lambda x: (x[0], x[1],x[2]), reverse=True)
    #将蛋糕按照美丽度、美味度和受欢迎度排序
    cakes = sorted(cakes, key=lambda x: (x[2], x[1],x[0]), reverse=True)
    #将蛋糕按照美丽度、美味度和受欢迎度排序
    cakes = sorted(cakes, key=lambda x: (x[1], x[0],x[2]), reverse=True)
    #print(cakes)
    #将蛋糕的美丽度、美味度和受欢迎度分为三个列表
    x = []
    y = []
    z = []
    for i in cakes:
        x.append(i[0])
        y.append(i[1])
        z.append(i[2])
    #print(x)
    #print(y)
    #print(z)
    #将蛋糕的美丽度、美味度和受欢迎度分为三个列表
    x = []
    y = []
    z = []
    for i in cakes:
        x.append(i[0])
        y.append(i[1])
        z.append(i[2])
    #print(x)
    #print(y)
    #print(z)
    #将蛋糕的美丽度、美味度和受欢迎度分为三个列表
    x = []
    y = []
    z = []
    for i in cakes:
        x.append(i[0])
