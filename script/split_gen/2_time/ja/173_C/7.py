def get_input_data():
    h, w, k = map(int, input().split())
    c = []
    for i in range(h):
        c.append(input())
    return h, w, k, c
