def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = i + 1
    C = [0] * N
    for i in range(N):
        C[i] = N - i
    D = [0] * N
    for i in range(N):
        D[i] = (i + 1) * (N - i)
    E = [0] * N
    for i in range(N):
        E[i] = A[i] * D[i]
    E.sort()
    F = [0] * N
    for i in range(N):
        F[i] = E[i] // D[i]
    print(F[(N - 1) // 2])

if __name__ == '__main__':
    main()