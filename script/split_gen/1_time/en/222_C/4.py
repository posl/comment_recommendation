def main():
    N, M = map(int, input().split())
    A = [list(input()) for _ in range(2 * N)]
    B = [list(range(1, 2 * N + 1))]
    for i in range(M):
        C = [0] * (2 * N)
        for j in range(N):
            if A[B[i][2 * j - 1] - 1][i] == A[B[i][2 * j] - 1][i]:
                C[B[i][2 * j - 1] - 1] += 1
                C[B[i][2 * j] - 1] += 1
            elif A[B[i][2 * j - 1] - 1][i] == 'G' and A[B[i][2 * j] - 1][i] == 'C':
                C[B[i][2 * j - 1] - 1] += 3
            elif A[B[i][2 * j - 1] - 1][i] == 'G' and A[B[i][2 * j] - 1][i] == 'P':
                C[B[i][2 * j] - 1] += 3
            elif A[B[i][2 * j - 1] - 1][i] == 'C' and A[B[i][2 * j] - 1][i] == 'G':
                C[B[i][2 * j] - 1] += 3
            elif A[B[i][2 * j - 1] - 1][i] == 'C' and A[B[i][2 * j] - 1][i] == 'P':
                C[B[i][2 * j - 1] - 1] += 3
            elif A[B[i][2 * j - 1] - 1][i] == 'P' and A[B[i][2 * j] - 1][i] == 'G':
                C[B[i][2 * j - 1] - 1] += 3
            elif A[B[i][2 * j - 1] - 1][i] == 'P' and A[B[i][2 * j] - 1][i] == 'C':
                C[B[i][2 * j] -
