def get_min_cost(N, T, routes):
    min_cost = T
    for route in routes:
        if route[1] <= T and route[0] < min_cost:
            min_cost = route[0]
    if min_cost == T:
        return "TLE"
    else:
        return min_cost

if __name__ == '__main__':
    get_min_cost()