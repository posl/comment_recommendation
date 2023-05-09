def solve():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    for i in range(n):
        for j in range(n):
            if a[i] == a[j]:
                continue
            if a[i] % a[j] != 0:
                continue
            if a[i] // a[j] not in d:
                continue
            cnt += d[a[i] // a[j]]
    print(cnt)
