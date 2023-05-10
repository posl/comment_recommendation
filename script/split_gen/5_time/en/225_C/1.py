def main():
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for i in range(N)]
    for i in range(N):
        for j in range(M):
            B[i][j] -= i * 7
    for i in range(N):
        for j in range(M):
            if B[i][j] <= 0 or B[i][j] > 7:
                print("No")
                return
            if i > 0 and B[i][j] <= B[i - 1][j]:
                print("No")
                return
            if j > 0 and B[i][j] <= B[i][j - 1]:
                print("No")
                return
    print("Yes")
