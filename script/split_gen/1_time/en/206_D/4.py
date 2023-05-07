def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A + [0]
    B = [0]*(N+1)
    for i in range(1, N+1):
        B[i] = A[i] - A[i+1]
    C = [0]*(N+1)
    for i in range(1, N+1):
        C[i] = B[i] - B[i-1]
    D = [0]*(N+1)
    for i in range(1, N+1):
        D[i] = C[i] - C[i-1]
    E = [0]*(N+1)
    for i in range(1, N+1):
        E[i] = D[i] - D[i-1]
    F = [0]*(N+1)
    for i in range(1, N+1):
        F[i] = E[i] - E[i-1]
    G = [0]*(N+1)
    for i in range(1, N+1):
        G[i] = F[i] - F[i-1]
    H = [0]*(N+1)
    for i in range(1, N+1):
        H[i] = G[i] - G[i-1]
    I = [0]*(N+1)
    for i in range(1, N+1):
        I[i] = H[i] - H[i-1]
    J = [0]*(N+1)
    for i in range(1, N+1):
        J[i] = I[i] - I[i-1]
    K = [0]*(N+1)
    for i in range(1, N+1):
        K[i] = J[i] - J[i-1]
    L = [0]*(N+1)
    for i in range(1, N+1):
        L[i] = K[i] - K[i-1]
    M = [0]*(N+1)
    for i in range(1, N+1):
        M[i] = L[i] - L[i-1]
    N = [0]*(N+1)
    for i in range(1, N+1):
        N[i] = M[i] - M[i-1]
