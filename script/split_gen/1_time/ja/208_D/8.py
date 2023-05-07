def main():
    N, M = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    A = [set() for _ in range(N)]
    for a, b, c in edges:
        A[a-1].add((b-1, c))
    ans = 0
    for k in range(N):
        for s in range(N):
            for t in range(N):
                if s == t:
                    continue
                dist = [float('inf')] * N
                dist[s] = 0
                for i in range(N):
                    for j in range(N):
                        if dist[j] == float('inf'):
                            continue
                        for b, c in A[j]:
                            if b > k:
                                continue
                            if dist[b] > dist[j] + c:
                                dist[b] = dist[j] + c
                if dist[t] != float('inf'):
                    ans += dist[t]
    print(ans)
