def min_cost(x_list, p):
    cost = 0
    for x in x_list:
        cost += (x - p) ** 2
    return cost
