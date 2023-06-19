def min_cost(n, a, b):
    cost = 0
    if n * a < b:
        cost = n * a
    else:
        cost = b
    return cost
