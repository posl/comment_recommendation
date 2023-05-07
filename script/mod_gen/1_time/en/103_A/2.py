def find_min_cost(a1, a2, a3):
    cost1 = abs(a2-a1) + abs(a3-a2)
    cost2 = abs(a3-a1) + abs(a2-a3)
    cost3 = abs(a1-a2) + abs(a3-a1)
    return min(cost1, cost2, cost3)

if __name__ == '__main__':
    find_min_cost()