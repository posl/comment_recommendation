def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted(A)
    B = [0] * N
    for i in range(N):
        B[i] = A[i] - i
    C = [0] * N
    for i in range(N):
        C[i] = B[i] - B[0]
    D = [0] * N
    for i in range(N):
        D[C[i]] += 1
    E = [0] * N
    for i in range(N):
        E[i] = E[i - 1] + D[i]
    for i in range(N):
        print(E[N - 1] - E[N - 1 - i] - (N - 1 - i) * D[N - 1 - i])

if __name__ == '__main__':
    main()