def get_input():
    N,T = map(int,input().split())
    routes = []
    for i in range(N):
        c,t = map(int,input().split())
        routes.append((c,t))
    return N,T,routes
