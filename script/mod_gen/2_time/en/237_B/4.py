def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    for j in range(W):
        for i in range(H):
            if i == H - 1:
                print(A[i][j])
            else:
                print(A[i][j], end=' ')

if __name__ == '__main__':
    main()