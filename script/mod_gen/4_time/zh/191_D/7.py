def f(x,y,r):
    from math import sqrt
    x1=int(x)
    y1=int(y)
    r1=int(r)
    count=0
    for i in range(x1-r1,x1+r1+1):
        for j in range(y1-r1,y1+r1+1):
            if sqrt((i-x)**2+(j-y)**2)<=r:
                count+=1
    return count

if __name__ == '__main__':
    f()