def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [A[i] + B[i] for i in range(N)]
    D = [i + 1 for i in range(N)]
    E = sorted(zip(A, D), reverse=True)
    F = sorted(zip(B, D), reverse=True)
    G = sorted(zip(C, D), reverse=True)
    H = []
    for i in range(X):
        H.append(E[i][1])
    for i in range(Y):
        if F[i][1] not in H:
            H.append(F[i][1])
    for i in range(Z):
        if G[i][1] not in H:
            H.append(G[i][1])
    H.sort()
    for i in range(X + Y + Z):
        print(H[i])

if __name__ == '__main__':
    main()