def calc_min_travel_cost(n, a, b):
    cost = 0
    if a * n < b:
        cost = a * n
    else:
        cost = b
    return cost

if __name__ == '__main__':
    calc_min_travel_cost()