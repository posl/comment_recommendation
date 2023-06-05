def solve(n,x):
    if n==0:
        return 0 if x<=0 else 1
    elif x<=1+level[n-1]:
        return solve(n-1,x-1)
    else:
        return patty[n-1]+1+solve(n-1,x-2-level[n-1])
n,x=map(int,input().split())
level=[1]*(n+1)
patty=[1]*(n+1)
for i in range(n):
    level[i+1]=level[i]*2+3
    patty[i+1]=patty[i]*2+1
print(solve(n,x))
