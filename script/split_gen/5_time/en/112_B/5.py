def get_input():
    n, t = map(int, input().split())
    routes = []
    for i in range(n):
        route = list(map(int, input().split()))
        routes.append(route)
    return t, routes
