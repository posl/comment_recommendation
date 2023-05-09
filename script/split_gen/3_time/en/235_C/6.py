def get_input():
    n, q = map(int, input().split(' '))
    a = list(map(int, input().split(' ')))
    queries = []
    for i in range(q):
        queries.append(list(map(int, input().split(' '))))
    return n, q, a, queries
