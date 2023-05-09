def main():
    n, m = map(int, input().split())
    p = [0] * m
    y = [0] * m
    for i in range(m):
        p[i], y[i] = map(int, input().split())
    p = [p[i] - 1 for i in range(m)]
    y = [y[i] - 1 for i in range(m)]
    d = dict()
    for i in range(m):
        if p[i] in d:
            d[p[i]].append(y[i])
        else:
            d[p[i]] = [y[i]]
    for k in d:
        d[k].sort()
    for i in range(m):
        print('{:06d}{:06d}'.format(p[i] + 1, d[p[i]].index(y[i]) + 1))

if __name__ == '__main__':
    main()