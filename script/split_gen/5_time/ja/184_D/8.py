def solve(a,b,c):
    if a==100 or b==100 or c==100:
        return 0
    if a==0 and b==0 and c==0:
        return 0
    ans=0
    ans+=a/(a+b+c)*(1+solve(a+1,b-1,c))
    ans+=b/(a+b+c)*(1+solve(a,b+1,c-1))
    ans+=c/(a+b+c)*(1+solve(a-1,b,c+1))
    return ans
a,b,c=map(int,input().split())
print(solve(a,b,c))
