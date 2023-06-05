def get_input():
    n, x = map(int, input().split())
    v_p = []
    for i in range(n):
        v_p.append(list(map(int, input().split())))
    return n, x, v_p
