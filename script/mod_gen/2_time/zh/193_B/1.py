def solve():
    N = int(input())
    stores = []
    for i in range(N):
        A, P, X = map(int, input().split())
        stores.append((A, P, X))
    min_cost = -1
    for i in range(N):
        A, P, X = stores[i]
        if X > 0:
            if min_cost == -1 or min_cost > P:
                min_cost = P
    print(min_cost)

if __name__ == '__main__':
    solve()