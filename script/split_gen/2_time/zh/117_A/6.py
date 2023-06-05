def solve():
    import sys
    from collections import defaultdict
    from heapq import heappush, heappop
    input = sys.stdin.readline
    N, K = map(int, input().split())
    sushi = defaultdict(list)
    for _ in range(N):
        t, d = map(int, input().split())
        sushi[t].append(d)
    for v in sushi.values():
        v.sort(reverse=True)
    # 最初のK個を選ぶ
    sushi_heap = []
    for v in sushi.values():
        if len(v) >= 2:
            heappush(sushi_heap, (-(v[0] + v[1]), 0, 1))
    # 最初のK個を選んだ時の美味しさの合計
    ans = sum(v[0] for v in sushi.values())
    ans += sum(-v[0] for v in sushi_heap[:K - len(sushi)])
    # K個の中から1個ずつ入れ替えていく
    for _ in range(K - len(sushi)):
        v, i, j = heappop(sushi_heap)
        ans -= v
        if j + 1 < len(sushi[sushi_heap[i][1]]):
            heappush(sushi_heap, (-(sushi[sushi_heap[i][1]][j] + sushi[sushi_heap[i][1]][j + 1]), i, j + 1))
    print(ans)
