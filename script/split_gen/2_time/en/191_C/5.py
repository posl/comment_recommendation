def get_input():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    return h, w, s
