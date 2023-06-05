def solve():
    N, K = map(int, input().split())
    sushi = []
    for _ in range(N):
        t, d = map(int, input().split())
        sushi.append((t, d))
    sushi.sort(key=lambda x: x[1], reverse=True)
    kind = set()
    kind_sushi = []
    ans = 0
    for i in range(K):
        ans += sushi[i][1]
        if sushi[i][0] in kind:
            kind_sushi.append(sushi[i][1])
        else:
            kind.add(sushi[i][0])
    ans += len(kind) ** 2
    kind_sushi.sort()
    for i in range(K, N):
        if sushi[i][0] in kind:
            continue
        if not kind_sushi:
            break
        ans += sushi[i][1] - kind_sushi.pop(0)
        kind.add(sushi[i][0])
    print(ans)
solve()
