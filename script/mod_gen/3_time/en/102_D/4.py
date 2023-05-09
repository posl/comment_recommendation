def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = [0] * N
    P[0] = A[0]
    for i in range(1, N):
        P[i] = P[i - 1] + A[i]
    Q = [0] * N
    Q[N - 1] = A[N - 1]
    for i in range(N - 2, -1, -1):
        Q[i] = Q[i + 1] + A[i]
    ans = 10 ** 9
    for i in range(1, N - 2):
        for j in range(i + 1, N - 1):
            ans = min(ans, max(P[i - 1], Q[j + 1], P[j - 1] - P[i - 1], P[N - 1] - P[j - 1]) - min(P[i - 1], Q[j + 1], P[j - 1] - P[i - 1], P[N - 1] - P[j - 1]))
    print(ans)

if __name__ == '__main__':
    main()