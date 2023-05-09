def main():
    n = int(input())
    shops = []
    for i in range(n):
        a, p, x = map(int, input().split())
        shops.append([a, p, x])
    min_price = -1
    for i in range(n):
        if shops[i][2] > 0:
            if min_price == -1:
                min_price = shops[i][1]
            else:
                min_price = min(min_price, shops[i][1])
    print(min_price)

if __name__ == '__main__':
    main()