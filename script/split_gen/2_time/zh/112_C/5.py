def getMinCost(n,t,route):
    minCost = 100000
    for i in range(n):
        if route[i][1] <= t:
            if route[i][0] < minCost:
                minCost = route[i][0]
    if minCost == 100000:
        print('TLE')
    else:
        print(minCost)
