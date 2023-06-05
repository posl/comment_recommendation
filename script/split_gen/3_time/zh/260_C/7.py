def solve(n,x,y):
    if x>y:
        return 0
    else:
        return (n-1)*(y-x)
n,x,y=map(int,input().split())
print(solve(n,x,y))
