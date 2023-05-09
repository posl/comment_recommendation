def main():
    N, T = map(int, input().split())
    routes = [list(map(int, input().split())) for _ in range(N)]
    routes = sorted(routes, key=lambda x: x[0])
    for cost, time in routes:
        if time <= T:
            print(cost)
            exit()
    print('TLE')
