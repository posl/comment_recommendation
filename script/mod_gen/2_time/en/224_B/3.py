def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if i < H - 1 and j < W - 1 and A[i][j] + A[i + 1][j + 1] > A[i + 1][j] + A[i][j + 1]:
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    main()