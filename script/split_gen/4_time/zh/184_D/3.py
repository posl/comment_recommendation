def solve(a,b,c):
    if a==0 and b==0 and c==0:
        return 0
    return a/(a+b+c)*(solve(a+1,b-1,c)+1)+b/(a+b+c)*(solve(a,b+1,c-1)+1)+c/(a+b+c)*(solve(a,b,c+1)+1)
a,b,c=map(int,input().split())
print(solve(a,b,c))
