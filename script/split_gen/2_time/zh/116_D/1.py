def solve():
    # N, K = map(int, input().split())
    # sushi = [list(map(int, input().split())) for _ in range(N)]
    N, K = 7, 4
    sushi = [[1, 1], [2, 1], [3, 1], [4, 6], [4, 5], [4, 5], [4, 5]]
    sushi.sort(key=lambda x: x[1], reverse=True)
    print(sushi)
    sushi.sort(key=lambda x: x[0])
    print(sushi)
    print('sushi', sushi)
    eat = sushi[:K]
    print('eat', eat)
    base = sum([i[1] for i in eat])
    print('base', base)
    kind = len(set([i[0] for i in eat]))
    print('kind', kind)
    ans = base + kind * kind
    print(ans)
