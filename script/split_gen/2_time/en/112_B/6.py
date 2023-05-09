def main():
    N, T = map(int, input().split())
    routes = [tuple(map(int, input().split())) for _ in range(N)]
    routes.sort(key=lambda x: x[0])
    min_cost = float('inf')
    for i in range(N):
        if routes[i][1] <= T:
            min_cost = min(min_cost, routes[i][0])
    if min_cost == float('inf'):
        print('TLE')
    else:
        print(min_cost)
