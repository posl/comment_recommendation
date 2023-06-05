def solve():
    N, K = map(int, input().split())
    sushi = []
    for i in range(N):
        t, d = map(int, input().split())
        sushi.append((t, d))
    sushi.sort(key=lambda x: x[1], reverse=True)
    kind = set()
    sum = 0
    for i in range(K):
        sum += sushi[i][1]
        kind.add(sushi[i][0])
    ans = sum + len(kind) ** 2
    for i in range(K, N):
        if sushi[i][0] not in kind:
            sum += sushi[i][1] - sushi[K - 1][1]
            kind.add(sushi[i][0])
            ans = max(ans, sum + len(kind) ** 2)
    print(ans)
solve()
