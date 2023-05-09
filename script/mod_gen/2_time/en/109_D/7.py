def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    print(H*W-1)
    for i in range(H):
        for j in range(W):
            if j < W-1:
                if A[i][j] % 2 == 1:
                    print(i+1, j+1, i+1, j+2)
                    A[i][j+1] += 1
            else:
                if A[i][j] % 2 == 1 and i < H-1:
                    print(i+1, j+1, i+2, j+1)
                    A[i+1][j] += 1

if __name__ == '__main__':
    main()