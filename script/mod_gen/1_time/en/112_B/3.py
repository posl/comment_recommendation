def main():
    n, t = map(int, input().split())
    routes = []
    for i in range(n):
        route = list(map(int, input().split()))
        if route[1] <= t:
            routes.append(route[0])
    if len(routes) == 0:
        print('TLE')
    else:
        print(min(routes))

if __name__ == '__main__':
    main()