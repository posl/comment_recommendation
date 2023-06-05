def get_min_cost(a1,a2,a3):
    cost = 1000000
    if a1 > a2:
        cost = a1 - a2
    else:
        cost = a2 - a1
    if a1 > a3:
        cost = cost + a1 - a3
    else:
        cost = cost + a3 - a1
    return cost

if __name__ == '__main__':
    get_min_cost()