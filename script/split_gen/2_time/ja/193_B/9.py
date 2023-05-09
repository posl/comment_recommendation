def main():
    N = int(input())
    shop = []
    for i in range(N):
        A, P, X = map(int, input().split())
        shop.append([A, P, X])
    shop.sort(key=lambda x: x[1])
    for i in range(N):
        if shop[i][2] - shop[i][0] > 0:
            print(shop[i][1])
            return
    print(-1)
