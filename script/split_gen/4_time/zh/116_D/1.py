def solve():
    # N, K = map(int, input().split())
    # sushi = []
    # for _ in range(N):
    #     t, d = map(int, input().split())
    #     sushi.append((t, d))
    N, K = 6, 5
    sushi = [(5, 1000000000), (2, 990000000), (3, 980000000), (6, 970000000), (6, 960000000), (4, 950000000)]
    sushi.sort(key=lambda x: -x[1])
    # print(sushi)
    # print()
    # print()
    # print()
