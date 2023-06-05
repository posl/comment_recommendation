def main():
    N = int(input())
    A = [list(map(int, input())) for _ in range(N)]
    ans = -1
    for i in range(N):
        for j in range(N):
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if di == 0 and dj == 0:
                        continue
                    tmp = A[i][j]
                    ni, nj = i + di, j + dj
                    for _ in range(N - 1):
                        if 0 <= ni < N and 0 <= nj < N:
                            tmp *= 10
                            tmp += A[ni][nj]
                            ni += di
                            nj += dj
                        else:
                            break
                    ans = max(ans, tmp)
    print(ans)
