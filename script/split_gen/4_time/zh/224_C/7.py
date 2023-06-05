def getArea(x1,y1,x2,y2,x3,y3):
    return abs(x1*y2+x2*y3+x3*y1-x1*y3-x2*y1-x3*y2)
N = int(input())
X = []
Y = []
for i in range(N):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)
ans = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            area = getArea(X[i],Y[i],X[j],Y[j],X[k],Y[k])
            if area > 0:
                ans += 1
print(ans)
