def min_cost(a1, a2, a3):
    min_cost = 100000000
    # 1 2 3
    cost = abs(a1-a2) + abs(a2-a3) + abs(a3-a1)
    if cost < min_cost:
        min_cost = cost
    # 1 3 2
    cost = abs(a1-a3) + abs(a3-a2) + abs(a2-a1)
    if cost < min_cost:
        min_cost = cost
    # 2 1 3
    cost = abs(a2-a1) + abs(a1-a3) + abs(a3-a2)
    if cost < min_cost:
        min_cost = cost
    # 2 3 1
    cost = abs(a2-a3) + abs(a3-a1) + abs(a1-a2)
    if cost < min_cost:
        min_cost = cost
    # 3 1 2
    cost = abs(a3-a1) + abs(a1-a2) + abs(a2-a3)
    if cost < min_cost:
        min_cost = cost
    # 3 2 1
    cost = abs(a3-a2) + abs(a2-a1) + abs(a1-a3)
    if cost < min_cost:
        min_cost = cost
    return min_cost

if __name__ == '__main__':
    min_cost()