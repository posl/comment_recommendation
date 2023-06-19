def solve(n,x):
    if n==0:
        return 0 if x<=0 else 1
    elif x<=1+2*burger[n-1]:
        return solve(n-1,x-1)
    else:
        return patty[n-1]+1+solve(n-1,x-2-burger[n-1])
n,x=map(int,input().split())
burger=[1]
patty=[1]
for i in range(n):
    burger.append(2*burger[-1]+3)
    patty.append(2*patty[-1]+1)
print(solve(n,x))
