def solve():
    N, X = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    cur = 0
    for i in range(N):
        cur += a[i]
        if cur > X:
            print("No")
            return
        cur += b[i] - a[i]
    if cur == X:
        print("Yes")
    else:
        print("No")
