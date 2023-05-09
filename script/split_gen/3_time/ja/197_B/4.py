def get_input_data():
    h, w, x, y = map(int, input().split())
    s = []
    for i in range(h):
        s.append(input())
    return h, w, x, y, s
