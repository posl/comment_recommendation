def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            T[i][j] += T[j][i]
            T[j][i] = T[i][j]
    for i in range(1, N):
        for j in range(i + 1, N):
            T[i][j] += T[j][i]
            T[j][i] = T[i][j]
    for i in range(1, N):
        for j in range(i + 1, N):
            T[i][j] += T[j][i]
            T[j][i] = T[i][j]
    for i in range(1, N):
        for j in range(i + 1, N):
            T[i][j] += T[j][i]
            T[j][i] = T[i][j]
    for i in range(1, N):
        for j in range(i + 1, N):
            T[i][j] += T[j][i]
            T[j][i] = T[i][j]
    for i in range(1, N):
        for j in range(i + 1, N):
            T[i][j] += T[j][i]
            T[j][i] = T[i][j]
    for i in range(1, N):
        for j in range(i + 1, N):
            T[i][j] += T[j][i]
            T[j][i] = T[i][j]
    for i in range(1, N):
        for j in range(i + 1, N):
            T[i][j] += T[j][i]
            T[j][i] = T[i][j]
    for i in range(1, N):
        for j in range(i + 1, N):
            T[i][j] += T[j][i]
            T[j][i] = T[i][j]
    for i in range(1, N):
        for j in range(i + 1, N):
            T[i][j] += T[j][i]
            T[j][i] = T[i][j]
    for
