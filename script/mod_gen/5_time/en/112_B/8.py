def get_data():
    n, t = list(map(int, input().split()))
    routes = []
    for i in range(n):
        c, t = list(map(int, input().split()))
        routes.append((c, t))
    return t, routes

if __name__ == '__main__':
    get_data()