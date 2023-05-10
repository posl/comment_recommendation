def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    for i in range(1, H):
        for j in range(1, W):
            if A[i-1][j-1] + A[i][j] > A[i][j-1] + A[i-1][j]:
                print('No')
                exit()
    print('Yes')

if __name__ == '__main__':
    main()