def solve():
    n, m, q = map(int, input().split())
    wv = [tuple(map(int, input().split())) for _ in range(n)]
    x = list(map(int, input().split()))
    query = [tuple(map(int, input().split())) for _ in range(q)]
    wv.sort(key=lambda x: x[1], reverse=True)
    for l, r in query:
        print(max_value(wv, x, l - 1, r))
