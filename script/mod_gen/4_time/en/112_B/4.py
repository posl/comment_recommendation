def main():
    N, T = map(int, input().split())
    routes = []
    for i in range(N):
        c, t = map(int, input().split())
        routes.append((c,t))
    routes.sort(key=lambda x: x[0])
    for c, t in routes:
        if t <= T:
            print(c)
            return
    print('TLE')

if __name__ == '__main__':
    main()