def main():
    N = int(input())
    A = list(map(int, input().split()))
    M = N * (N + 1) // 2
    M2 = (M + 1) // 2
    M3 = (M + 2) // 2
    B = []
    for i in range(N):
        B.append((A[i], i))
    B.sort()
    C = [0] * N
    for i in range(M):
        C[B[i][1]] = i
    S = [0] * (N + 1)
    S2 = [0] * (N + 1)
    S3 = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + C[i]
        S2[i + 1] = S2[i] + (C[i] < M2)
        S3[i + 1] = S3[i] + (C[i] < M3)
    ans = 0
    for i in range(N):
        ans += (S2[N] - S2[i]) * (C[i] + 1) - (S[i + 1] - S2[i])
        ans += (S[i + 1] - S3[i]) - (S3[N] - S3[i]) * (C[i] + 1)
    ans //= M
    print(ans)
main()

if __name__ == '__main__':
    main()