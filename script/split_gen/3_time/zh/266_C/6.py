def judge_convex(a,b,c,d):
    #a,b,c,d是四个点的坐标
    #判断四边形是否是凸的
    #计算向量ab,ac,ad
    ab=(b[0]-a[0],b[1]-a[1])
    ac=(c[0]-a[0],c[1]-a[1])
    ad=(d[0]-a[0],d[1]-a[1])
    #计算向量ab和ac的叉积
    abXac=ab[0]*ac[1]-ab[1]*ac[0]
    #计算向量ab和ad的叉积
    abXad=ab[0]*ad[1]-ab[1]*ad[0]
    #计算向量ac和ad的叉积
    acXad=ac[0]*ad[1]-ac[1]*ad[0]
    if abXac*abXad>0 and abXac*acXad>0:
        return True
    else:
        return False
