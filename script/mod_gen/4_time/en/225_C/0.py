def main():
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if B[i][j] % 7 == 0:
                B[i][j] = B[i][j] // 7
            else:
                B[i][j] = B[i][j] // 7 + 1
    for i in range(N):
        for j in range(M):
            if B[i][j] == 1:
                for k in range(i, N):
                    for l in range(j, M):
                        if B[k][l] != 1 + k - i + 7 * (l - j):
                            print("No")
                            return
                print("Yes")
                return
    print("No")

if __name__ == '__main__':
    main()