def main():
    N = int(input())
    shops = []
    for i in range(N):
        shops.append(list(map(int, input().split())))
    min_price = -1
    for i in range(N):
        if shops[i][2] > 0 and (min_price == -1 or min_price > shops[i][1]):
            min_price = shops[i][1]
    print(min_price)
