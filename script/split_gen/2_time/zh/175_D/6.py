def solve(x,k,d):
    if x<0:
        x=-x
    if k*d<x:
        return x-k*d
    else:
        if (k-(x//d))%2==0:
            return x%d
        else:
            return d-x%d
x,k,d=map(int,input().split())
print(solve(x,k,d))
