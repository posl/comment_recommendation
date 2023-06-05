def get_min_cost(n, m, x, costs, understand):
    costs = [costs[i] for i in range(n) if understand[i] < x]
    if len(costs) == 0:
        return 0
    min_cost = min(costs)
    min_cost_index = costs.index(min_cost)
    understand = [understand[i] + understand[min_cost_index] for i in range(n)]
    return min_cost + get_min_cost(n, m, x, costs, understand)
n, m, x = map(int, input().split())
costs = []
understand = []
for i in range(n):
    cost, *understand_level = map(int, input().split())
    costs.append(cost)
    understand.append(sum(understand_level))
print(get_min_cost(n, m, x, costs, understand))
