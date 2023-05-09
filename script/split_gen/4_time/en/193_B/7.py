def get_input():
    n = int(input())
    shops = []
    for i in range(n):
        a, p, x = map(int, input().split())
        shops.append([a, p, x])
    return n, shops
