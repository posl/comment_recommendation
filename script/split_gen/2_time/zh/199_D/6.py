def solve():
    n,m = map(int,input().split())
    e = [[] for _ in range(n)]
    for _ in range(m):
        a,b = map(int,input().split())
        e[a-1].append(b-1)
        e[b-1].append(a-1)
    r = 0
    for i in range(3**n):
        c = [0]*n
        for j in range(n):
            c[j] = (i//3**j)%3
        flg = True
        for j in range(n):
            for k in e[j]:
                if c[j] == c[k]:
                    flg = False
        if flg:
            r += 1
    print(r)
