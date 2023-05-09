def get_input():
    h, w = map(int, input().split())
    s = []
    for _ in range(h):
        s.append(input())
    return h, w, s
