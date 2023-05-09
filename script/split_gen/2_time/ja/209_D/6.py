def init():
    global N, Q, a, b, c, d
    N, Q = map(int, input().split())
    a = [0] * (N-1)
    b = [0] * (N-1)
    for i in range(N-1):
        a[i], b[i] = map(int, input().split())
    c = [0] * Q
    d = [0] * Q
    for i in range(Q):
        c[i], d[i] = map(int, input().split())
