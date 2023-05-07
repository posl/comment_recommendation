def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    for i in range(H):
        for j in range(W):
            a, b, c, d = A[i][j], A[i][j], A[i][j], A[i][j]
            if i > 0:
                a = A[i-1][j]
            if j > 0:
                b = A[i][j-1]
            if i < H-1:
                c = A[i+1][j]
            if j < W-1:
                d = A[i][j+1]
            if not a+b <= c+d:
                print('No')
                return
    print('Yes')

if __name__ == '__main__':
    main()