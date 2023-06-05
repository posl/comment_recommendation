def is_convex(a,b,c,d):
    if ((b[0]-a[0])*(c[1]-b[1])-(c[0]-b[0])*(b[1]-a[1]))*((c[0]-b[0])*(d[1]-c[1])-(d[0]-c[0])*(c[1]-b[1]))<0:
        return False
    if ((c[0]-b[0])*(d[1]-c[1])-(d[0]-c[0])*(c[1]-b[1]))*((d[0]-c[0])*(a[1]-d[1])-(a[0]-d[0])*(d[1]-c[1]))<0:
        return False
    if ((d[0]-c[0])*(a[1]-d[1])-(a[0]-d[0])*(d[1]-c[1]))*((a[0]-d[0])*(b[1]-a[1])-(b[0]-a[0])*(a[1]-d[1]))<0:
        return False
    if ((a[0]-d[0])*(b[1]-a[1])-(b[0]-a[0])*(a[1]-d[1]))*((b[0]-a[0])*(c[1]-b[1])-(c[0]-b[0])*(b[1]-a[1]))<0:
        return False
    return True
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
d=list(map(int,input().split()))

if __name__ == '__main__':
    is_convex()