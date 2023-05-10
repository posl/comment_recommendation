def main():
    n = int(input())
    a = []
    p = []
    x = []
    for i in range(n):
        a1, p1, x1 = map(int, input().split())
        a.append(a1)
        p.append(p1)
        x.append(x1)
    min_price = -1
    for i in range(n):
        if x[i] > 0:
            if min_price == -1:
                min_price = p[i]
            else:
                min_price = min(min_price, p[i])
    print(min_price)

if __name__ == '__main__':
    main()