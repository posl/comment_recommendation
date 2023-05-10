def area(x1,y1,x2,y2,x3,y3):
    return abs((x2-x1)*(y3-y1)-(x3-x1)*(y2-y1))/2
N = int(input())
X = []
Y = []
for i in range(N):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)
count = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if area(X[i],Y[i],X[j],Y[j],X[k],Y[k]) > 0:
                count += 1
print(count)
