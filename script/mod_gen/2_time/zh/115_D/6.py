def solve(n,x):
    if n==0:
        return 0
    elif x==1:
        return 0
    elif x<=1+f[n-1]:
        return solve(n-1,x-1)
    elif x==2+f[n-1]:
        return p[n-1]+1
    elif x<=2+2*f[n-1]:
        return p[n-1]+1+solve(n-1,x-2-f[n-1])
    else:
        return 2*p[n-1]+1
n,x=map(int,input().split())
f=[1]
p=[1]
for i in range(n):
    f.append(2*f[i]+3)
    p.append(2*p[i]+1)
print(solve(n,x))
