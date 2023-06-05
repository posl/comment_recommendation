def read_data():
    #读取数据
    #输入格式
    #N S D
    #X_1 Y_1
    #.
    #.
    #.
    #X_N Y_N
    #输出格式
    #如果高桥能对怪物造成伤害，打印Yes；否则，打印No。
    #返回值
    #N:法术数量
    #S:伤害时间
    #D:伤害力度
    #X:法术施展时间列表
    #Y:法术伤害力度列表
    N,S,D = map(int,input().split())
    X = []
    Y = []
    for i in range(N):
        x,y = map(int,input().split())
        X.append(x)
        Y.append(y)
    return N,S,D,X,Y
