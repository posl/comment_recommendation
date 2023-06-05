def solve():
    n,m = map(int,input().split())
    a = []
    b = []
    c = []
    d = []
    for i in range(m):
        ai,bi = map(int,input().split())
        a.append(ai)
        b.append(bi)
    for i in range(m):
        ci,di = map(int,input().split())
        c.append(ci)
        d.append(di)
    for i in range(n):
        for j in range(n):
            if i != j:
                if (i+1 in a and j+1 in a) or (i+1 in b and j+1 in b):
                    if (i+1 in c and j+1 in c) or (i+1 in d and j+1 in d):
                        pass
                    else:
                        print('No')
                        return
                if (i+1 in c and j+1 in c) or (i+1 in d and j+1 in d):
                    if (i+1 in a and j+1 in a) or (i+1 in b and j+1 in b):
                        pass
                    else:
                        print('No')
                        return
    print('Yes')
    return
solve()
