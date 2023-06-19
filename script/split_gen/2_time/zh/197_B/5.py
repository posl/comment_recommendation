def get_input():
    h, w, x, y = map(int, input().split())
    s = []
    for i in range(h):
        s.append(input())
    return h, w, x, y, s
