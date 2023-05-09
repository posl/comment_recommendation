def distance(x,y):
    d = 0
    for i in range(len(x)):
        d += (x[i]-y[i])*(x[i]-y[i])
    return int(d**0.5)
n,d = map(int,input().split())
x = [list(map(int,input().split())) for i in range(n)]
ans = 0
for i in range(n):
    for j in range(i+1,n):
        if distance(x[i],x[j])**2 == distance(x[i],x[j])*distance(x[i],x[j]):
            ans += 1
print(ans)
