def main():
    n = int(input())
    a = []
    x = []
    y = []
    for i in range(n):
        a.append(int(input()))
        x.append([])
        y.append([])
        for _ in range(a[i]):
            tmp = list(map(int, input().split()))
            x[i].append(tmp[0])
            y[i].append(tmp[1])
    ans = 0
    for i in range(1, 1 << n):
        ok = True
        for j in range(n):
            if (i >> j) & 1:
                for k in range(a[j]):
                    if ((i >> (x[j][k] - 1)) & 1) ^ y[j][k]:
                        ok = False
        if ok:
            ans = max(ans, bin(i).count("1"))
    print(ans)

if __name__ == '__main__':
    main()