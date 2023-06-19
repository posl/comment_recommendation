def selectRoute(N, T, routes):
    minCost = 1001
    for i in range(N):
        if routes[i][1] <= T and routes[i][0] < minCost:
            minCost = routes[i][0]
    if minCost == 1001:
        return "TLE"
    else:
        return minCost
