def solve():
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    # a = [180, 186, 189, 191, 218]
    # n = 5
    d = {}
    for i in range(n):
        for j in range(i+1, n):
            if (a[i]+a[j])%200 not in d:
                d[(a[i]+a[j])%200] = [[i, j]]
            else:
                d[(a[i]+a[j])%200].append([i, j])
    for k, v in d.items():
        if len(v) >= 2:
            print('Yes')
            print(len(v[0]), end=' ')
            for i in v[0]:
                print(i+1, end=' ')
            print()
            print(len(v[1]), end=' ')
            for i in v[1]:
                print(i+1, end=' ')
            print()
            return
    print('No')
solve()
