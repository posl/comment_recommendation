def solve():
    N, K = map(int, input().split())
    sushi = []
    for _ in range(N):
        t, d = map(int, input().split())
        sushi.append((t, d))
    sushi.sort(key=lambda x: x[1], reverse=True)
    from collections import defaultdict
    from heapq import heappush, heappop
    kinds = defaultdict(list)
    for t, d in sushi:
        kinds[t].append(d)
    kinds = sorted(kinds.items(), key=lambda x: -x[1][0])
    kinds = [(t, d[0]) for t, d in kinds]
    kind = 0
    heap = []
    for i in range(K):
        t, d = sushi[i]
        if kinds[kind][0] == t:
            pass
        else:
            heappush(heap, -d)
    ans = sum([d for t, d in sushi[:K]]) + len(kinds)**2
    for i in range(K, N):
        t, d = sushi[i]
        if kinds[kind][0] == t:
            continue
        else:
            if heap:
                min_d = -heappop(heap)
                ans = max(ans, sum([d for t, d in sushi[:K]]) + len(kinds)**2 - min_d + d)
                kind += 1
            else:
                break
    return ans
print(solve())

if __name__ == '__main__':
    solve()