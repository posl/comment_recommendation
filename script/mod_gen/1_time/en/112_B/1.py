def main():
    N, T = map(int, input().split())
    routes = []
    for i in range(N):
        c, t = map(int, input().split())
        if t <= T:
            routes.append(c)
    if len(routes) == 0:
        print("TLE")
    else:
        print(min(routes))

if __name__ == '__main__':
    main()