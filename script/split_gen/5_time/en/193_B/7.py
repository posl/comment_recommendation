def solve():
    N = int(input())
    shops = []
    for i in range(N):
        A, P, X = map(int, input().split())
        shops.append((A, P, X))
    min_price = 10**9 + 1
    for i in range(N):
        A, P, X = shops[i]
        if X > 0:
            min_price = min(min_price, P)
    if min_price == 10**9 + 1:
        print(-1)
    else:
        print(min_price)
