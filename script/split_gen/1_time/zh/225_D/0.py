def get_query():
    N, Q = map(int, input().split())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    return N, Q, query
