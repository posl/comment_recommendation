def get_input():
    n, c = map(int, input().split())
    d = []
    for i in range(c):
        d.append([int(i) for i in input().split()])
    c = []
    for i in range(n):
        c.append([int(i) for i in input().split()])
    return n, c, d
