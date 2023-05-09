def get_input():
    n,t = map(int,input().split())
    routes = []
    for i in range(n):
        c_i,t_i = map(int,input().split())
        routes.append((c_i,t_i))
    return n,t,routes
