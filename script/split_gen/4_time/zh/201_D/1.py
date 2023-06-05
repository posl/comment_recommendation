def get_input():
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(input())
    return h, w, a
