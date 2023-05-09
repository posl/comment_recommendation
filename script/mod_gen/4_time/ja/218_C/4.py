def rotate90(S):
    N = len(S)
    T = [['.'] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            T[i][j] = S[N-1-j][i]
    return T

if __name__ == '__main__':
    rotate90()