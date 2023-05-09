def distance(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5
N = int(input())
x = []
y = []
for i in range(N):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)
max_distance = 0
for i in range(N):
    for j in range(i+1,N):
        dist = distance(x[i],y[i],x[j],y[j])
        if dist > max_distance:
            max_distance = dist
print(max_distance)
