def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if A[i][j] > A[i][W - 1 - j] + A[H - 1 - i][j]:
                print('No')
                return
    print('Yes')

if __name__ == '__main__':
    main()