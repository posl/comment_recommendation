def get_input():
    n, q = map(int, input().split())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    s = []
    for i in range(q):
        s.append(list(map(int, input().split())))
    return n, q, l, s
