def solve(a,b,c,x):
    if x <= a:
        return 1
    elif x >= b+1:
        return 0
    else:
        return c/(b-a)
a,b,c,x = map(int, input().split())
print(solve(a,b,c,x))
