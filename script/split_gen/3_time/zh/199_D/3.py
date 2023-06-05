def solve():
    n,m = map(int,input().split())
    e = [[] for _ in range(n)]
    for i in range(m):
        a,b = map(int,input().split())
        e[a-1].append(b-1)
        e[b-1].append(a-1)
    ans = 0
    for i in range(3**n):
        ok = True
        for j in range(n):
            for k in e[j]:
                if (i // 3**k) % 3 == (i // 3**j) % 3:
                    ok = False
        if ok:
            ans += 1
    print(ans)
solve()
