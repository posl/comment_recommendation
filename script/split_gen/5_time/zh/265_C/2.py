def get_input():
    h, w = map(int, input().split())
    g = []
    for i in range(h):
        g.append(input())
    return h, w, g
