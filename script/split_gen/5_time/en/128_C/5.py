def get_input():
    n, m = map(int, input().split())
    k = []
    s = []
    for i in range(m):
        k.append(list(map(int, input().split())))
        s.append(list(map(int, input().split())))
    p = list(map(int, input().split()))
    return n, m, k, s, p
