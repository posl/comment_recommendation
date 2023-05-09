def main():
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            B[i][j] -= i * 7 + j + 1
    for i in range(N - 1):
        for j in range(M - 1):
            if B[i][j] != B[i][j + 1] or B[i][j] != B[i + 1][j] or B[i][j] != B[i + 1][j + 1]:
                print('No')
                exit()
    print('Yes')
