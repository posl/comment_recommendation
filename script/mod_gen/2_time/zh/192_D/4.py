def solve(x,m):
    d = int(max(x))
    #print(d)
    ans = 0
    for i in range(d,m+1):
        if int(x,int(d+1))<=m:
            ans+=1
    print(ans)
x = input()
m = int(input())
solve(x,m)
