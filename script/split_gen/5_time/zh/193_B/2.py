def solve():
    N = int(input())
    shops = []
    for i in range(N):
        A, P, X = map(int, input().split())
        shops.append([A, P, X])
    min_cost = -1
    for i in range(N):
        A, P, X = shops[i]
        if X > 0:
            if min_cost == -1:
                min_cost = P
            else:
                min_cost = min(min_cost, P)
    print(min_cost)
