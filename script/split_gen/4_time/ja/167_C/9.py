def calcCost(costs, algos):
    cost = 0
    for i in range(len(costs)):
        cost += costs[i] * algos[i]
    return cost
