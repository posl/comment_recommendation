def solve(n,x):
    if n==0:
        return 0 if x<=0 else 1
    elif x<=1+size[n-1]:
        return solve(n-1,x-1)
    else:
        return patty[n-1]+1+solve(n-1,x-2-size[n-1])
n,x=map(int,input().split())
size=[1]
patty=[1]
for i in range(n):
    size.append(size[-1]*2+3)
    patty.append(patty[-1]*2+1)
print(solve(n,x))
