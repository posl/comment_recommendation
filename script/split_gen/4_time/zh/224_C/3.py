def area(x1,y1,x2,y2,x3,y3):
    return abs((x1-x3)*(y2-y3)-(x2-x3)*(y1-y3))
n=int(input())
x=[]
y=[]
for _ in range(n):
    a,b=map(int,input().split())
    x.append(a)
    y.append(b)
ans=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            s=area(x[i],y[i],x[j],y[j],x[k],y[k])
            if s!=0:
                ans+=1
print(ans)
