def problems130_c():
    #读取输入
    W,H,x,y = map(int,input().split())
    #计算面积
    print(W*H/2,1 if x==W/2 and y==H/2 else 0)
