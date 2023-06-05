def search_route(routes, T):
    routes = sorted(routes, key=lambda x: x[0])
    routes = sorted(routes, key=lambda x: x[1])
    print(routes)
    cost = 0
    for route in routes:
        if route[1] <= T:
            cost = route[0]
            break
    return cost
