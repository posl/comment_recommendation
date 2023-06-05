def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    B = [[0 for _ in range(H)] for _ in range(W)]
    for i in range(W):
        for j in range(H):
            B[i][j] = A[j][i]
    for i in range(W):
        for j in range(H):
            print(B[i][j], end=" ")
        print("")

if __name__ == '__main__':
    main()