def get_input():
    N,T = map(int,input().split())
    routes = []
    for i in range(N):
        c,t = map(int,input().split())
        routes.append((c,t))
    return N,T,routes

if __name__ == '__main__':
    get_input()