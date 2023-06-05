def main():
    #读取数据
    a,b,c,d,e,f,x = map(int,input().split())
    #计算高桥和青木的行走距离
    tq = 0
    tq += (a+b)*c
    tq += a*(x//(a+b))
    tq += min(a,x%(a+b))
    ta = 0
    ta += (d+e)*f
    ta += d*(x//(d+e))
    ta += min(d,x%(d+e))
    #比较
    if tq > ta:
        print("高桥")
    elif tq < ta:
        print("青木")
    else:
        print("画")
