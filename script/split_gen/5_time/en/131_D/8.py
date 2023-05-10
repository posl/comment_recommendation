def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # print(A)
    # print(B)
    C = [0] * N
    for i in range(N):
        C[i] = A[i] + B[i]
    # print(C)
    D = [0] * N
    for i in range(N):
        D[i] = C[i] - B[i]
    # print(D)
    E = [0] * N
    for i in range(N):
        E[i] = C[i] + B[i]
    # print(E)
    F = [0] * N
    for i in range(N):
        F[i] = D[i] + B[i]
    # print(F)
    G = [0] * N
    for i in range(N):
        G[i] = E[i] + B[i]
    # print(G)
    H = [0] * N
    for i in range(N):
        H[i] = F[i] + B[i]
    # print(H)
    I = [0] * N
    for i in range(N):
        I[i] = G[i] + B[i]
    # print(I)
    J = [0] * N
    for i in range(N):
        J[i] = H[i] + B[i]
    # print(J)
    K = [0] * N
    for i in range(N):
        K[i] = I[i] + B[i]
    # print(K)
    L = [0] * N
    for i in range(N):
        L[i] = J[i] + B[i]
    # print(L)
    M = [0] * N
    for i in range(N):
        M[i] = K[i] + B[i]
    # print(M)
    N = [0] * N
    for i in range(N):
        N[i] = L[i] + B[i]
    # print(N)
    O = [0] * N
    for i in range(N):
        O[i] = M[i] + B[i]
    # print(O)
    P = [0] * N
    for i in range(N):
