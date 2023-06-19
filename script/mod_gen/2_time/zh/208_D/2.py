def main():
    N, M = map(int, input().split())
    A, B, C = [], [], []
    for i in range(M):
        a, b, c = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
    # Floyd-Warshall algorithm
    # 1. Initialize the distance matrix.
    dist = [[float('inf') for _ in range(N + 1)] for _ in range(N + 1)]
    for i in range(N + 1):
        dist[i][i] = 0
    for i in range(M):
        dist[A[i]][B[i]] = C[i]
    # 2. Update the distance matrix.
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    # 3. Count the number of triplets (s, t, k) such that f(s, t, k) > 0.
    count = 0
    for s in range(1, N + 1):
        for t in range(1, N + 1):
            for k in range(1, N + 1):
                if dist[s][t] == dist[s][k] + dist[k][t]:
                    count += 1
    # 4. Print the answer.
    print(count)

if __name__ == '__main__':
    main()