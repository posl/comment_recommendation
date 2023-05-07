def main():
    N, M = map(int, input().split())
    if N == 2:
        print(0)
        return
    from collections import defaultdict
    d = defaultdict(list)
    for _ in range(M):
        a, b = map(int, input().split())
        d[a].append(b)
        d[b].append(a)
    #print(d)
    import heapq
    q = []
    heapq.heappush(q, (0, 1))
    visited = set()
    visited.add(1)
    while q:
        cost, node = heapq.heappop(q)
        if node == N:
            print(cost)
            return
        for n in d[node]:
            if n not in visited:
                visited.add(n)
                heapq.heappush(q, (cost+1, n))
    print(0)

if __name__ == '__main__':
    main()