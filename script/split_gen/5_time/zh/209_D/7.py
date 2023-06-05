def get_input():
    n, q = map(int, input().split())
    roads = []
    for i in range(n-1):
        roads.append(list(map(int, input().split())))
    queries = []
    for i in range(q):
        queries.append(list(map(int, input().split())))
    return n, q, roads, queries
