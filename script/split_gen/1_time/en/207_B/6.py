def solve(a,b,c,d):
    if a<=b*d:
        return 0
    return (a-b*d-1)//(b*c-b)+1
a,b,c,d=map(int,input().split())
print(solve(a,b,c,d))
