def main():
    n = int(input())
    shops = []
    for i in range(0, n):
        shops.append([int(x) for x in input().split()])
    min = -1
    for i in range(0, n):
        if shops[i][2] > 0:
            if min == -1 or shops[i][1] < min:
                min = shops[i][1]
    print(min)

if __name__ == '__main__':
    main()