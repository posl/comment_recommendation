def solve():
    N, Q = map(int, input().split())
    a = [0] * N
    b = [0] * N
    for i in range(Q):
        t, a[i], b[i] = map(int, input().split())
        a[i] -= 1
        b[i] -= 1
    c = [0] * N
    for i in range(Q):
        if t == 1:
            c[a[i]] |= 1 << b[i]
        elif t == 2:
            c[a[i]] &= ~(1 << b[i])
        elif t == 3:
            if c[a[i]] & (1 << b[i]) and c[b[i]] & (1 << a[i]):
                print("Yes")
            else:
                print("No")
        else:
            assert(False)
