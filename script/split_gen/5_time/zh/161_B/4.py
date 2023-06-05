def problem161_b():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    total = sum(a)
    for i in range(m):
        if a[i] * 4 * m < total:
            print('否')
            return
    print('是')
