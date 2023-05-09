def solve(a,b,c):
    if a*c <= b:
        return c
    else:
        return b//a
a,b,c = map(int,input().split())
print(solve(a,b,c))
