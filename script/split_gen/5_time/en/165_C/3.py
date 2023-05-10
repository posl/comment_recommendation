def get_input():
    n, m, q = map(int, input().split())
    abcd = []
    for i in range(q):
        abcd.append(list(map(int, input().split())))
    return n, m, q, abcd
