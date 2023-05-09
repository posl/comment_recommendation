def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    C = [0] * N
    D = [0] * N
    E = [0] * N
    for i in range(N):
        B[i] = B[i - 1] + A[i]
        E[i] = E[i - 1] + A[N - 1 - i]
    for i in range(1, N - 2):
        C[i] = C[i - 1] + A[i]
    for i in range(2, N - 1):
        D[i] = D[i - 1] + A[N - i]
    ans = 10 ** 9
    for i in range(1, N - 2):
        ans = min(ans, max(B[i], C[i], D[N - i], E[N - i]) - min(B[i], C[i], D[N - i], E[N - i]))
    print(ans)

if __name__ == '__main__':
    main()