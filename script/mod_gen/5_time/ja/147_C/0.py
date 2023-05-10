def main():
    n = int(input())
    a = []
    x = []
    y = []
    for i in range(n):
        a.append(int(input()))
        x.append([])
        y.append([])
        for j in range(a[i]):
            xi, yi = map(int, input().split())
            x[i].append(xi)
            y[i].append(yi)
    ans = 0
    for i in range(2**n):
        ok = True
        for j in range(n):
            if (i >> j) & 1:
                for k in range(a[j]):
                    if y[j][k] != ((i >> (x[j][k]-1)) & 1):
                        ok = False
        if ok:
            ans = max(ans, bin(i).count("1"))
    print(ans)

if __name__ == '__main__':
    main()