def get_input():
    N, Q = map(int, input().split())
    road = []
    for i in range(N-1):
        a, b = map(int, input().split())
        road.append([a, b])
    query = []
    for i in range(Q):
        c, d = map(int, input().split())
        query.append([c, d])
    return N, Q, road, query
