def f(x,y):
    return 0.5*abs(x[0]*y[1]-x[1]*y[0])
n=int(input())
x=[]
y=[]
for i in range(n):
    a,b=map(int,input().split())
    x.append(a)
    y.append(b)
ans=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            ans=max(ans,f((x[i],y[i]),(x[j],y[j]))+f((x[j],y[j]),(x[k],y[k]))+f((x[k],y[k]),(x[i],y[i])))
print(ans)
