def find_route(routes, time):
    min_cost = time + 1
    for route in routes:
        if route[1] <= time:
            if route[0] < min_cost:
                min_cost = route[0]
    if min_cost > time:
        return 'TLE'
    else:
        return min_cost
