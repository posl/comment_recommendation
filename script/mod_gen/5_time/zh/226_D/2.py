def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    res = 0
    for i in range(n):
        for j in range(i+1, n):
            a = x[i]-x[j]
            b = y[i]-y[j]
            c = 0
            d = 0
            for k in range(n):
                for l in range(k+1, n):
                    if x[k]-x[l] == a and y[k]-y[l] == b:
                        c += 1
                    if x[k]-x[l] == -a and y[k]-y[l] == -b:
                        d += 1
            res = max(res, n-c, n-d)
    print(res)
    return

if __name__ == '__main__':
    main()