def get_min_cost(a1, a2, a3):
    cost = 0
    if a1 > a2:
        cost += a1 - a2
        a1 = a2
    if a1 > a3:
        cost += a1 - a3
        a1 = a3
    if a2 < a1:
        cost += a2 - a1
        a2 = a1
    if a2 > a3:
        cost += a2 - a3
        a2 = a3
    return cost
