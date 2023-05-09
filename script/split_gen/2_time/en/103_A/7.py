def min_cost(costs):
    costs.sort()
    return costs[1] - costs[0] + costs[2] - costs[1]
