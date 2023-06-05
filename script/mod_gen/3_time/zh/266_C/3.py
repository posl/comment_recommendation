def is_convex(a,b,c,d):
    if a[0]*b[1]+b[0]*c[1]+c[0]*d[1]+d[0]*a[1]-a[1]*b[0]-b[1]*c[0]-c[1]*d[0]-d[1]*a[0]>0:
        return 1
    else:
        return 0
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))

if __name__ == '__main__':
    is_convex()