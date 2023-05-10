def main():
    n, m = map(int, input().split())
    p = [0] * m
    y = [0] * m
    for i in range(m):
        p[i], y[i] = map(int, input().split())
    #print(p)
    #print(y)
    d = {}
    for i in range(m):
        if p[i] in d:
            d[p[i]].append(y[i])
        else:
            d[p[i]] = [y[i]]
    #print(d)
    for i in d.keys():
        d[i] = sorted(d[i])
    #print(d)
    for i in range(m):
        print(str(p[i]).zfill(6) + str(d[p[i]].index(y[i]) + 1).zfill(6))

if __name__ == '__main__':
    main()