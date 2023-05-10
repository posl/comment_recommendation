def solve():
    n, m = map(int, input().split())
    d = {}
    for i in range(m):
        u, v = map(int, input().split())
        if u not in d:
            d[u] = set()
        if v not in d:
            d[v] = set()
        d[u].add(v)
        d[v].add(u)
    if len(d[1]) != 1 or len(d[n]) != 1:
        print('No')
    else:
        for i in range(2, n):
            if len(d[i]) != 2:
                print('No')
                return
        print('Yes')

if __name__ == '__main__':
    solve()