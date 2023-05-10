def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0,0)
    B = [0] * (N + 1)
    for i in range(1, N + 1):
        B[i] = A[A[i]]
    C = [0] * (N + 1)
    for i in range(1, N + 1):
        C[i] = B[B[i]]
    D = [0] * (N + 1)
    for i in range(1, N + 1):
        D[i] = C[C[i]]
    E = [0] * (N + 1)
    for i in range(1, N + 1):
        E[i] = D[D[i]]
    F = [0] * (N + 1)
    for i in range(1, N + 1):
        F[i] = E[E[i]]
    G = [0] * (N + 1)
    for i in range(1, N + 1):
        G[i] = F[F[i]]
    H = [0] * (N + 1)
    for i in range(1, N + 1):
        H[i] = G[G[i]]
    I = [0] * (N + 1)
    for i in range(1, N + 1):
        I[i] = H[H[i]]
    J = [0] * (N + 1)
    for i in range(1, N + 1):
        J[i] = I[I[i]]
    K = [0] * (N + 1)
    for i in range(1, N + 1):
        K[i] = J[J[i]]
    L = [0] * (N + 1)
    for i in range(1, N + 1):
        L[i] = K[K[i]]
    M = [0] * (N + 1)
    for i in range(1, N + 1):
        M[i] = L[L[i]]
    N = [0] * (N + 1)
    for i in range(1, N + 1):
        N[i] = M[M[i]]
    O = [0] * (N + 1

if __name__ == '__main__':
    main()