def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    B = [0 for _ in range(M + 1)]
    for i in range(N):
        for j in range(1, len(A[i])):
            B[A[i][j]] += 1
    ans = 0
    for i in range(1, M + 1):
        if B[i] == N:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()