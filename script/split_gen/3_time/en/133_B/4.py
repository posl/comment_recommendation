def get_input():
    n, d = map(int, input().split())
    x = []
    for i in range(n):
        x.append(list(map(int, input().split())))
    return n, d, x
