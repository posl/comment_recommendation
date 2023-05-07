def main():
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            B[i][j] -= 1
    for i in range(10 ** 100 - N + 1):
        for j in range(7 - M + 1):
            if all(B[k][l] == i * 7 + j + l for k in range(N) for l in range(M)):
                print('Yes')
                return
    print('No')
