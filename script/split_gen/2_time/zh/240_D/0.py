def solve():
    N,X = map(int,input().split())
    a = []
    b = []
    for i in range(N):
        ai,bi = map(int,input().split())
        a.append(ai)
        b.append(bi)
    now = 0
    for i in range(N):
        if now + a[i] <= X and now + b[i] >= X:
            print('Yes')
            return
        now += b[i]
    print('No')
