def findMinCost(N, T, cost, time):
    minCost = 1000 * 1000
    for i in range(N):
        if time[i] <= T and cost[i] < minCost:
            minCost = cost[i]
    return minCost

if __name__ == '__main__':
    findMinCost()