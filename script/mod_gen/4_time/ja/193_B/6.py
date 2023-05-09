def main():
    n = int(input())
    a = []
    p = []
    x = []
    for _ in range(n):
        a_i, p_i, x_i = map(int, input().split())
        a.append(a_i)
        p.append(p_i)
        x.append(x_i)
    min_price = 10 ** 9
    for i in range(n):
        if x[i] > a[i]:
            min_price = min(min_price, p[i])
    if min_price == 10 ** 9:
        print(-1)
    else:
        print(min_price)

if __name__ == '__main__':
    main()