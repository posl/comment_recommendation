def get_input():
    n,c = map(int, input().split())
    d = []
    for _ in range(c):
        d.append(list(map(int, input().split())))
    c = []
    for _ in range(n):
        c.append(list(map(int, input().split())))
    return n,c,d
