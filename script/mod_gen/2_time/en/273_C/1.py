def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = sorted(A)
    C = [0] * N
    for i in range(N):
        C[i] = B.index(A[i])
    D = [0] * N
    for i in range(N):
        D[C[i]] += 1
    E = [0] * N
    for i in range(N):
        E[i] = D[i] * (D[i] - 1) // 2
    F = [0] * N
    for i in range(N):
        F[C[i]] += 1
        if i != 0:
            F[i] += F[i - 1]
    G = [0] * N
    for i in range(N):
        G[i] = F[i] * (F[i] - 1) // 2
    for i in range(N):
        print(G[i] - E[i])

if __name__ == '__main__':
    main()