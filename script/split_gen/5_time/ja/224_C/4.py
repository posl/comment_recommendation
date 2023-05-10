def get_area(x1,y1,x2,y2,x3,y3):
    return abs((x2-x1)*(y3-y1)-(x3-x1)*(y2-y1))/2
N = int(input())
xy = []
for i in range(N):
    xy.append(list(map(int,input().split())))
ans = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if get_area(xy[i][0],xy[i][1],xy[j][0],xy[j][1],xy[k][0],xy[k][1]) != 0:
                ans += 1
print(ans)
