def solve():
    n = int(input())
    shops = []
    for i in range(n):
        a, p, x = map(int, input().split())
        shops.append((a, p, x))
    min_price = 1000000000
    for shop in shops:
        a, p, x = shop
        if x > 0:
            min_price = min(min_price, p)
    if min_price == 1000000000:
        print(-1)
    else:
        print(min_price)
