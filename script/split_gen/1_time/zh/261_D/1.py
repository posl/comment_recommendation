def main():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    cy = []
    for i in range(m):
        cy.append(list(map(int,input().split())))
    cy.sort(key=lambda x:x[1],reverse=True)
    #print(cy)
    #print(x)
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
            if x[i] == cy[0][0]:
                for k in range(m):
                    if j+1 == cy[k][0]:
                        dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j+1-cy[k][0]]+cy[k][1])
    print(dp[n][n])
