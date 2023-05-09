def main():
    N, M = map(int, input().split())
    A = []
    B = []
    C = []
    for _ in range(M):
        a, b, c = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
    ans = 0
    for k in range(1, N+1):
        for s in range(1, N+1):
            for t in range(1, N+1):
                if s == t:
                    continue
                dist = [float('inf') for _ in range(N+1)]
                dist[s] = 0
                for i in range(M):
                    if A[i] == s and B[i] <= k:
                        dist[B[i]] = min(dist[B[i]], C[i])
                    elif B[i] == s and A[i] <= k:
                        dist[A[i]] = min(dist[A[i]], C[i])
                ans += dist[t]
    print(ans)
