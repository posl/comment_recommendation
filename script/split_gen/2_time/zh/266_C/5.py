def is_convex():
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    x3,y3 = map(int,input().split())
    x4,y4 = map(int,input().split())
    #计算向量
    v1 = [x2-x1,y2-y1]
    v2 = [x3-x2,y3-y2]
    v3 = [x4-x3,y4-y3]
    v4 = [x1-x4,y1-y4]
    #计算叉积
    c1 = v1[0]*v2[1]-v1[1]*v2[0]
    c2 = v2[0]*v3[1]-v2[1]*v3[0]
    c3 = v3[0]*v4[1]-v3[1]*v4[0]
    c4 = v4[0]*v1[1]-v4[1]*v1[0]
    #判断符号
    if c1>0 and c2>0 and c3>0 and c4>0:
        return True
    elif c1<0 and c2<0 and c3<0 and c4<0:
        return True
    else:
        return False
