def get_min_cost(n, c, a, b, cost):
    # 1. get the min cost for each day
    # 2. get the min cost for each day with Snuke Prime
    # 3. get the min cost for each day without Snuke Prime
    # 4. get the min cost for each day
    # 5. get the min cost for the whole period
    min_cost = [0] * n
    min_cost[0] = min(cost[0], c)
    for i in range(1, n):
        min_cost[i] = min_cost[i-1] + min(cost[i], c)
    min_cost_with_prime = [0] * n
    min_cost_with_prime[0] = min_cost[0]
    for i in range(1, n):
        min_cost_with_prime[i] = min_cost_with_prime[i-1] + min(cost[i], c)
        if a[i] - b[i-1] > 1:
            min_cost_with_prime[i] = min(min_cost_with_prime[i], min_cost[i-1] + c)
    min_cost_without_prime = [0] * n
    min_cost_without_prime[0] = cost[0]
    for i in range(1, n):
        min_cost_without_prime[i] = min_cost_without_prime[i-1] + cost[i]
    min_cost_with_prime_2 = [0] * n
    min_cost_with_prime_2[0] = min_cost_without_prime[0]
    for i in range(1, n):
        min_cost_with_prime_2[i] = min_cost_with_prime_2[i-1] + cost[i]
        if a[i] - b[i-1] > 1:
            min_cost_with_prime_2[i] = min(min_cost_with_prime_2[i], min_cost_without_prime[i-1] + c)
    #print(min_cost)
    #print(min_cost_with_prime)
    #print(min_cost_without_prime)
    #print(min_cost_with_prime_2)
    return min(min_cost_with_prime[n-1], min_cost_with_prime_2[n-1])
