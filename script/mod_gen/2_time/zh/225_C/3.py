def main():
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    for i in range(1, N):
        for j in range(1, M):
            B[i][j] -= B[0][0] - i * 7 - j
    for i in range(1, N):
        if B[i][0] != B[i-1][0] + 7:
            print("No")
            return
    for j in range(1, M):
        if B[0][j] != B[0][j-1] + 1:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()