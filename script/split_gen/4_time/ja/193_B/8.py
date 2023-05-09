def main():
    n = int(input())
    stores = [list(map(int, input().split())) for _ in range(n)]
    min_price = 10 ** 9 + 1
    for store in stores:
        time = store[0]
        price = store[1]
        stock = store[2]
        if stock > 0:
            min_price = min(min_price, price)
    if min_price == 10 ** 9 + 1:
        print(-1)
    else:
        print(min_price)
