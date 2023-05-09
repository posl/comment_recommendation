def main():
    N = int(input())
    shop = []
    for i in range(N):
        A, P, X = map(int, input().split())
        shop.append([A, P, X])
    shop.sort(key=lambda x: x[0])
    for a, p, x in shop:
        if x - a > 0:
            print(p)
            return
    print(-1)

if __name__ == '__main__':
    main()