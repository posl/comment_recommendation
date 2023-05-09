def main():
    n,t = map(int,input().split())
    routes = []
    for _ in range(n):
        c_i,t_i = map(int,input().split())
        if t_i <= t:
            routes.append([c_i,t_i])
    if len(routes) == 0:
        print("TLE")
    else:
        routes.sort(key=lambda x:x[0])
        print(routes[0][0])

if __name__ == '__main__':
    main()