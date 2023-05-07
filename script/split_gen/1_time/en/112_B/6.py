def get_input():
    n, t = map(int, input().split())
    routes = []
    for i in range(n):
        c, t_i = map(int, input().split())
        routes.append((c, t_i))
    return n, t, routes
