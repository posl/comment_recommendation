def solve():
    n=int(input())
    x,y=map(int,input().split())
    a=[]
    b=[]
    for i in range(n):
        ai,bi=map(int,input().split())
        a.append(ai)
        b.append(bi)
    dp=[[[False for i in range(301)]for j in range(301)]for k in range(n+1)]
    dp[0][0][0]=True
    for i in range(n):
        for j in range(n+1):
            for k in range(n+1):
                if dp[i][j][k]:
                    dp[i+1][j][k]=True
                    if j+a[i]<=n:
                        dp[i+1][j+a[i]][k]=True
                    if k+b[i]<=n:
                        dp[i+1][j][k+b[i]]=True
                    if j+a[i]<=n and k+b[i]<=n:
                        dp[i+1][j+a[i]][k+b[i]]=True
    ans=-1
    for i in range(n+1):
        for j in range(n+1):
            if dp[n][i][j] and i>=x and j>=y:
                ans=i+j
                break
    print(ans)

if __name__ == '__main__':
    solve()