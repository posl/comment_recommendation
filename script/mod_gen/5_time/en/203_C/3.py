def problem203_c():
    n, k = map(int, input().split())
    d = dict()
    for i in range(n):
        a, b = map(int, input().split())
        if a not in d:
            d[a] = 0
        d[a] += b
    l = sorted(d.items())
    for i in range(len(l)):
        if k >= l[i][0]:
            k += l[i][1]
        else:
            print(k)
            return
    print(k)
    return

if __name__ == '__main__':
    problem203_c()