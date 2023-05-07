def main():
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    if N == 1 and M == 1:
        print("Yes")
        return
    if N == 1:
        for i in range(1, M):
            if B[0][i] - B[0][i - 1] != 1:
                print("No")
                return
        print("Yes")
        return
    if M == 1:
        for i in range(1, N):
            if B[i][0] - B[i - 1][0] != 7:
                print("No")
                return
        print("Yes")
        return
    for i in range(1, N):
        for j in range(1, M):
            if B[i][j] - B[i - 1][j] != 7 or B[i][j] - B[i][j - 1] != 1:
                print("No")
                return
    print("Yes")
