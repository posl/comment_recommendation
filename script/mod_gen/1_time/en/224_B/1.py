def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if i == H - 1 and j == W - 1:
                break
            elif i == H - 1:
                if A[i][j] > A[i][j + 1]:
                    print("No")
                    return
            elif j == W - 1:
                if A[i][j] > A[i + 1][j]:
                    print("No")
                    return
            else:
                if A[i][j] > A[i][j + 1] or A[i][j] > A[i + 1][j]:
                    print("No")
                    return
    print("Yes")

if __name__ == '__main__':
    main()