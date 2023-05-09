def main():
    N, K = map(int, input().split())
    sushi = []
    for _ in range(N):
        t, d = map(int, input().split())
        sushi.append((d, t))
    sushi.sort(reverse=True)
    # print(sushi)
    kinds = set()
    ans = 0
    for i in range(K):
        d, t = sushi[i]
        ans += d
        kinds.add(t)
    ans += len(kinds) ** 2
    # print(ans)
    for i in range(K, N):
        d, t = sushi[i]
        if len(kinds) == K:
            break
        if t in kinds:
            continue
        ans += d
        kinds.add(t)
        ans += 2 * len(kinds) - 1
        # print(ans)
    print(ans)
