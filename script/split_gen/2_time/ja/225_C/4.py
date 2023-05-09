def main():
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for i in range(N)]
    for i in range(N):
        for j in range(M):
            B[i][j] -= 1
    for i in range(N - 1):
        for j in range(M - 1):
            if B[i][j] // 7 != B[i + 1][j] // 7:
                print("No")
                return
            if B[i][j] % 7 != B[i][j + 1] % 7:
                print("No")
                return
    print("Yes")
