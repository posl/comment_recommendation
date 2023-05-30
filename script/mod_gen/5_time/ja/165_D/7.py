def solve(a,b,n):
    if n<b:
        return int(a*n/b)
    else:
        return int(a*(b-1)/b)
a,b,n = map(int,input().split())
print(solve(a,b,n))
