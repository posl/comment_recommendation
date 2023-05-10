def get_input():
    n, m, q = map(int, input().split())
    wv = []
    for _ in range(n):
        wv.append(list(map(int, input().split())))
    x = list(map(int, input().split()))
    query = []
    for _ in range(q):
        query.append(list(map(int, input().split())))
    return n, m, q, wv, x, query

if __name__ == '__main__':
    get_input()