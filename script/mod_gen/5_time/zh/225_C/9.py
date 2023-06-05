def main():
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    for i in range(1, N):
        for j in range(1, M):
            if B[i][j] != B[i - 1][j - 1] + 7:
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    main()