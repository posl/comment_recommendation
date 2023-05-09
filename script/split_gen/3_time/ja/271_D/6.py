def main():
    N,S=map(int,input().split())
    a,b=[],[]
    for i in range(N):
        a_i,b_i=map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    dp=[[0 for j in range(S+1)] for i in range(N+1)]
    dp[0][0]=1
    for i in range(N):
        for j in range(S+1):
            if j-a[i]>=0:
                dp[i+1][j]=max(dp[i][j],dp[i][j-a[i]]+b[i])
            else:
                dp[i+1][j]=max(dp[i][j],dp[i][j]+b[i])
    if dp[N][S]==S:
        print("Yes")
        ans=""
        for i in range(N):
            if dp[N-i-1][S-a[N-i-1]]==S-b[N-i-1]:
                ans="H"+ans
                S-=a[N-i-1]
            else:
                ans="T"+ans
        print(ans)
    else:
        print("No")
