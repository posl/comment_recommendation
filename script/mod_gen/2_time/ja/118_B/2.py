def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    B = [0] * M
    for i in range(N):
        for j in range(1, A[i][0] + 1):
            B[A[i][j] - 1] += 1
    print(sum(1 for i in range(M) if B[i] == N))

if __name__ == '__main__':
    main()