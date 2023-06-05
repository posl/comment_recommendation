def check_convex(a,b,c,d):
    #计算向量ab和bc的叉积
    x1=b[0]-a[0]
    y1=b[1]-a[1]
    x2=c[0]-b[0]
    y2=c[1]-b[1]
    z1=x1*y2-x2*y1
    #计算向量bc和cd的叉积
    x1=c[0]-b[0]
    y1=c[1]-b[1]
    x2=d[0]-c[0]
    y2=d[1]-c[1]
    z2=x1*y2-x2*y1
    #计算向量cd和da的叉积
    x1=d[0]-c[0]
    y1=d[1]-c[1]
    x2=a[0]-d[0]
    y2=a[1]-d[1]
    z3=x1*y2-x2*y1
    #计算向量da和ab的叉积
    x1=a[0]-d[0]
    y1=a[1]-d[1]
    x2=b[0]-a[0]
    y2=b[1]-a[1]
    z4=x1*y2-x2*y1
    #如果z1 z2 z3 z4都是正数或者都是负数，那么就是凸四边形
    if (z1>0 and z2>0 and z3>0 and z4>0) or (z1<0 and z2<0 and z3<0 and z4<0):
        return True
    else:
        return False

if __name__ == '__main__':
    check_convex()