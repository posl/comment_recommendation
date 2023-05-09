def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for i in range(N):
        B[i] = A[i] - A[i - 1]
    B[N] = A[N - 1] - A[0]
    B = [0] + B
    C = [0] * (N + 1)
    for i in range(1, N + 1):
        C[i] = C[i - 1] + B[i]
    D = [0] * (N + 1)
    for i in range(1, N + 1):
        D[i] = D[i - 1] + C[i]
    E = [0] * (N + 1)
    for i in range(1, N + 1):
        E[i] = E[i - 1] + D[i]
    for i in range(1, N + 1):
        print(E[N] - E[i] + E[i - 1] + B[i] * N, end=' ')
    print()
