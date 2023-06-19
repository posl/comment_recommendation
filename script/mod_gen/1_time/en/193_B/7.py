def main():
    N = int(input())
    shops = []
    for i in range(N):
        A, P, X = map(int, input().split())
        shops.append([A, P, X])
    shops.sort(key=lambda x: x[0])
    for shop in shops:
        if shop[2] - shop[0] > 0:
            return shop[1]
    return -1
print(main())
