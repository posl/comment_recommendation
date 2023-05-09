def rotate(S):
    N = len(S)
    T = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            T[j][N - 1 - i] = S[i][j]
    return T

if __name__ == '__main__':
    rotate()