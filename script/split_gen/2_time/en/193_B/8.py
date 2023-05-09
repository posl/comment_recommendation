def main():
    N = int(input())
    shops = []
    for i in range(N):
        shops.append(list(map(int, input().split())))
    shops.sort(key=lambda x: x[0])
    for i in range(N):
        if shops[i][2] > shops[i][1]:
            print(shops[i][1])
            return
    print(-1)
