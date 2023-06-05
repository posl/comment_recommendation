def solve():
    N, K = map(int, input().split())
    sushi = []
    for i in range(N):
        t, d = map(int, input().split())
        sushi.append((t, d))
    sushi.sort(key=lambda x: x[1], reverse=True)
    # print(sushi)
    types = set()
    sum_d = 0
    for t, d in sushi[:K]:
        sum_d += d
        types.add(t)
    # print(types)
    # print(sum_d)
    ans = sum_d + len(types)**2
    # print(ans)
    for t, d in sushi[K:]:
        if t not in types:
            sum_d += d
            types.add(t)
            ans = max(ans, sum_d + len(types)**2)
    print(ans)
