def get_input():
    l, q = map(int, input().split())
    queries = []
    for _ in range(q):
        queries.append(tuple(map(int, input().split())))
    return l, q, queries
