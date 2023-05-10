def solve():
    N, K = map(int, input().split())
    sushi = [tuple(map(int, input().split())) for _ in range(N)]
    sushi.sort(key=lambda x: x[1], reverse=True)
    from collections import defaultdict
    kind = defaultdict(int)
    kind_list = []
    for t, d in sushi[:K]:
        kind[t] += 1
        if kind[t] == 1:
            kind_list.append(t)
    kind_list.sort()
    kind_list.reverse()
    ans = sum([d for t, d in sushi[:K]]) + len(kind_list)**2
    for i in range(K, N):
        t, d = sushi[i]
        if t in kind:
            continue
        if not kind_list:
            break
        kind[t] += 1
        kind_list.append(t)
        kind_list.sort()
        kind_list.reverse()
        kind_list.pop()
        ans = max(ans, sum([d for t, d in sushi[:i+1]]) + len(kind_list)**2)
    print(ans)
