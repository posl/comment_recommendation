def distance(x,y):
    d = 0
    for i in range(len(x)):
        d += (x[i]-y[i])**2
    return d
n,d = map(int,input().split())
x = [list(map(int,input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(i+1,n):
        if distance(x[i],x[j])**0.5 % 1 == 0:
            ans += 1
print(ans)
