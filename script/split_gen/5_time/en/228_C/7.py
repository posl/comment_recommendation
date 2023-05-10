def problems228_c():
    n,k = map(int, input().split())
    p = [list(map(int, input().split())) for i in range(n)]
    for i in range(n):
        p[i].append(sum(p[i]))
    p.sort(key=lambda x: x[3], reverse=True)
    for i in range(n):
        if i < k:
            print('Yes')
        else:
            print('No')
