def find():
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] + a
    d = {}
    for i in range(1, n + 1):
        d[a[i]] = i
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            b = a[i] + a[j]
            if b % 200 in d:
                if d[b % 200] != i and d[b % 200] != j:
                    print('Yes')
                    print('1', i)
                    print('1', d[b % 200])
                    return
    print('No')
    return
find()
