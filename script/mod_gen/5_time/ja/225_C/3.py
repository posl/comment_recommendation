def main():
    N, M = map(int, input().split())
    B = []
    for i in range(N):
        B.append(list(map(int, input().split())))
    for i in range(1, N):
        for j in range(1, M):
            if B[i][j] - B[i - 1][j] != B[i][j - 1] - B[i - 1][j - 1]:
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    main()