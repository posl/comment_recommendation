def get_input():
    h, w = map(int, input().split())
    s = []
    t = []
    for i in range(h):
        s.append(input())
    for i in range(h):
        t.append(input())
    return h, w, s, t
