def get_input():
    n, q = input().split()
    n = int(n)
    q = int(q)
    seq = []
    for i in range(n):
        seq.append(input().split())
    query = []
    for i in range(q):
        query.append(input().split())
    return n, q, seq, query
