def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(M)]
    edge = [0] * (N + 1)
    for i in range(M):
        u, v = A[i]
        edge[u] += 1
        edge[v] += 1
    print("Yes" if all([edge[i] % 2 == 0 for i in range(1, N + 1)]) else "No")

if __name__ == '__main__':
    main()