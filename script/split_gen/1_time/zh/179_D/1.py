def get_input():
    n, k = map(int, input().split())
    seg = []
    for i in range(k):
        seg.append(list(map(int, input().split())))
    return n, k, seg
