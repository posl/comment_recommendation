def isConvex(a,b,c,d):
    #print(a,b,c,d)
    #print(a[0],b[0],c[0],d[0])
    #print(a[1],b[1],c[1],d[1])
    #print((b[0]-a[0])*(c[1]-b[1]))
    #print((b[1]-a[1])*(c[0]-b[0]))
    #print((b[0]-a[0])*(c[1]-b[1])-(b[1]-a[1])*(c[0]-b[0]))
    #print((c[0]-b[0])*(d[1]-c[1]))
    #print((c[1]-b[1])*(d[0]-c[0]))
    #print((c[0]-b[0])*(d[1]-c[1])-(c[1]-b[1])*(d[0]-c[0]))
    #print((d[0]-c[0])*(a[1]-d[1]))
    #print((d[1]-c[1])*(a[0]-d[0]))
    #print((d[0]-c[0])*(a[1]-d[1])-(d[1]-c[1])*(a[0]-d[0]))
    #print((a[0]-d[0])*(b[1]-a[1]))
    #print((a[1]-d[1])*(b[0]-a[0]))
    #print((a[0]-d[0])*(b[1]-a[1])-(a[1]-d[1])*(b[0]-a[0]))
    if (b[0]-a[0])*(c[1]-b[1])-(b[1]-a[1])*(c[0]-b[0])>0:
        if (c[0]-b[0])*(d[1]-c[1])-(c[1]-b[1])*(d[0]-c[0])>0:
            if (d[0]-c[0])*(a[1]-d[1])-(d[1]-c[1])*(a[0]-d[0])>0

if __name__ == '__main__':
    isConvex()