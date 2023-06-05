def getDistance(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)
n = int(input())
x = [0]*n
y = [0]*n
p = [0]*n
for i in range(n):
    x[i],y[i],p[i] = map(int,input().split())
