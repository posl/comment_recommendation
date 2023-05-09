def main():
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    A = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            A[i][j] = (i - 1) * 7 + j + 1
    for i in range(N):
        for j in range(M):
            if A[i][j] != B[i][j]:
                print("No")
                return
    print("Yes")
