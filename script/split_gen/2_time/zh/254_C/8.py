def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = sorted(a)
    if k == 1:
        for i in range(n):
            if a[i] != b[i]:
                print('No')
                return
        print('Yes')
        return
    for i in range(n - k):
        if a[i] == b[i]:
            continue
        if a[i] == b[i + k] and a[i + k] == b[i]:
            a[i], a[i + k] = a[i + k], a[i]
            continue
        print('No')
        return
    for i in range(n - k, n):
        if a[i] != b[i]:
            print('No')
            return
    print('Yes')
    return
solve()
