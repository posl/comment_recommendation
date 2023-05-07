def rotate(S):
    N = len(S)
    T = [[None]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            T[j][N-i-1] = S[i][j]
    return T

if __name__ == '__main__':
    rotate()