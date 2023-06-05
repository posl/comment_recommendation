def get_input():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    query = []
    for i in range(q):
        query.append(list(map(int, input().split())))
    return n, a, q, query
