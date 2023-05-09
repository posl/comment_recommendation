def solve(n,c,d,cs):
    #n is the number of rows and columns
    #c is the number of colors
    #d is the cost of changing a color from j to i
    #cs is the initial colors of the grid
    #returns the minimum cost of changing the colors of the grid
    #so that the grid is a good grid
    
    #dp[i][j] is the minimum cost of changing the colors of the grid
    #so that the grid is a good grid
    #and the color of the first i rows is j
    dp = [[float('inf')]*c for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(c):
            for k in range(c):
                if (i+j)%3 != (i+k)%3:
                    dp[i+1][k] = min(dp[i+1][k],dp[i][j]+d[j][k])
    return min(dp[n])
