def main():
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = list(map(int, input().split()))
    #print(a,b,c,d)
    #print(a[0],a[1])
    #print(b[0],b[1])
    #print(c[0],c[1])
    #print(d[0],d[1])
    #print(a[0]-b[0],a[1]-b[1])
    #print(b[0]-c[0],b[1]-c[1])
    #print(c[0]-d[0],c[1]-d[1])
    #print(d[0]-a[0],d[1]-a[1])
    #print((a[0]-b[0])*(b[1]-c[1])-(a[1]-b[1])*(b[0]-c[0]))
    #print((b[0]-c[0])*(c[1]-d[1])-(b[1]-c[1])*(c[0]-d[0]))
    #print((c[0]-d[0])*(d[1]-a[1])-(c[1]-d[1])*(d[0]-a[0]))
    #print((d[0]-a[0])*(a[1]-b[1])-(d[1]-a[1])*(a[0]-b[0]))
    if (a[0]-b[0])*(b[1]-c[1])-(a[1]-b[1])*(b[0]-c[0]) > 0 and (b[0]-c[0])*(c[1]-d[1])-(b[1]-c[1])*(c[0]-d[0]) > 0 and (c[0]-d[0])*(d[1]-a[1])-(c[1]-d[1])*(d[0]-a[0]) > 0 and (d[0]-a[0])*(a[1]-b[1])-(d[1]-a[1])*(a[0]-b[0]) > 0:
        print("Yes")
    else:

if __name__ == '__main__':
    main()