def main():
    H, W = map(int, input().split())
    A = [[0] * W for _ in range(H)]
    for i in range(H):
        A[i] = list(map(int, input().split()))
    for i in range(H):
        for j in range(W):
            if i + 1 < H:
                if A[i][j] + A[i + 1][j] > A[i + 1][j] + A[i][j]:
                    print("No")
                    return
            if j + 1 < W:
                if A[i][j] + A[i][j + 1] > A[i][j + 1] + A[i][j]:
                    print("No")
                    return
    print("Yes")
    return

if __name__ == '__main__':
    main()