def solve():
    import heapq
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    q = []
    for i in range(X):
        for j in range(Y):
            for k in range(Z):
                if i * j * k < K:
                    heapq.heappush(q, -(A[i] + B[j] + C[k]))
                else:
                    break
    for _ in range(K):
        print(-heapq.heappop(q))

if __name__ == '__main__':
    solve()