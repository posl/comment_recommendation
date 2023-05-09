def get_input():
    n, m, q = map(int, input().split())
    lr = [list(map(int, input().split())) for i in range(m)]
    pq = [list(map(int, input().split())) for i in range(q)]
    return n, m, q, lr, pq
