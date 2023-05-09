def check(x1,y1,x2,y2,x3,y3):
    if x1==x2 and x1==x3:
        return True
    if x1==x2:
        return False
    if x1==x3:
        return False
    if x2==x3:
        return False
    if y1==y2 and y1==y3:
        return True
    if y1==y2:
        return False
    if y1==y3:
        return False
    if y2==y3:
        return False
    if (y2-y1)*(x3-x1)==(y3-y1)*(x2-x1):
        return True
    return False
N = int(input())
xy = []
for i in range(N):
    x,y = map(int,input().split())
    xy.append((x,y))
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if check(xy[i][0],xy[i][1],xy[j][0],xy[j][1],xy[k][0],xy[k][1]):
                print("Yes")
                exit()
print("No")
