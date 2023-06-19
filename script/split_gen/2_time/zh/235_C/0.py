def get_input():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    xk = []
    for _ in range(q):
        xk.append(list(map(int, input().split())))
    return n, q, a, xk
