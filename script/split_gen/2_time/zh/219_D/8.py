def solve():
    N = int(input())
    X,Y = map(int,input().split())
    AB = []
    for i in range(N):
        A,B = map(int,input().split())
        AB.append((A,B))
    dp = [[False]*(Y+1) for _ in range(X+1)]
    dp[0][0] = True
    for A,B in AB:
        for x in range(X,-1,-1):
            for y in range(Y,-1,-1):
                if x-A >= 0 and y-B >= 0:
                    dp[x][y] = dp[x][y] or dp[x-A][y-B]
    ans = float('inf')
    for x in range(X+1):
        for y in range(Y+1):
            if dp[x][y]:
                ans = min(ans,x+y)
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)
solve()
