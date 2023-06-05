def main():
    n, m, t = map(int, input().split())
    a = list(map(int, input().split()))
    xy = [list(map(int, input().split())) for _ in range(m)]
    x = [xy[i][0] for i in range(m)]
    y = [xy[i][1] for i in range(m)]
    now = 1
    for i in range(n-1):
        if now in x:
            t += y[x.index(now)]
        t -= a[i]
        if t <= 0:
            print('No')
            exit()
        now += 1
    print('Yes')

if __name__ == '__main__':
    main()