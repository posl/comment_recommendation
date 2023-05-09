def convex(a,b,c,d):
    if (b[0]-a[0])*(c[1]-b[1])-(b[1]-a[1])*(c[0]-b[0])>0:
        if (b[0]-a[0])*(d[1]-b[1])-(b[1]-a[1])*(d[0]-b[0])>0:
            if (d[0]-c[0])*(a[1]-d[1])-(d[1]-c[1])*(a[0]-d[0])>0:
                if (d[0]-c[0])*(b[1]-d[1])-(d[1]-c[1])*(b[0]-d[0])>0:
                    return 'Yes'
    return 'No'
a,b,c,d = [],[],[],[]
a.append(list(map(int,input().split())))
b.append(list(map(int,input().split())))
c.append(list(map(int,input().split())))
d.append(list(map(int,input().split())))
print(convex(a[0],b[0],c[0],d[0]))

if __name__ == '__main__':
    convex()