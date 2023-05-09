def main():
    N, T = [int(x) for x in input().split()]
    routes = [tuple(int(x) for x in input().split()) for _ in range(N)]
    routes.sort(key = lambda x: x[1])
    min_cost = 1001
    for cost, time in routes:
        if time > T:
            break
        min_cost = min(min_cost, cost)
    print(min_cost if min_cost < 1001 else "TLE")

if __name__ == '__main__':
    main()