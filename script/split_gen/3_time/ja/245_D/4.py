def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0 for i in range(M+1)]
    for i in range(N+M, N, -1):
        B[M-(N+M-i)] = C[i]
        for j in range(N, -1, -1):
            C[i-(N-j)] -= A[j]*B[M-(N+M-i)]
    for i in range(M, 0, -1):
        B[M-i] = C[i]/A[N]
        for j in range(N, -1, -1):
            C[i-(N-j)] -= A[j]*B[M-i]
    for i in range(M+1):
        print(int(B[i]), end=" ")
    print()
