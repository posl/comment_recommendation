def f(x,y):
    return abs(x)+abs(y)
n=int(input())
town=[]
for i in range(n):
    x,y=map(int,input().split())
    town.append((x,y))
    
town.sort()
ans=0
for i in range(n-1):
    for j in range(i+1,n):
        x1,y1=town[i]
        x2,y2=town[j]
        ans=max(ans,f(x2-x1,y2-y1))
print(ans)
