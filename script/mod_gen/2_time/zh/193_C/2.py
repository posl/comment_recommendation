def main():
    n = int(input())
    shops = []
    for i in range(n):
        a, p, x = map(int, input().split())
        shops.append((a, p, x))
    min_price = -1
    for shop in shops:
        if shop[2] > 0:
            if min_price == -1:
                min_price = shop[1]
            else:
                min_price = min(min_price, shop[1])
    print(min_price)

if __name__ == '__main__':
    main()