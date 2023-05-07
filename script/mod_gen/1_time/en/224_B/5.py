def main():
    H, W = map(int, input().split())
    A = [[0] * W for _ in range(H)]
    for i in range(H):
        A[i] = list(map(int, input().split()))
    for i in range(H):
        for j in range(W):
            if i < H-1 and j < W-1:
                if A[i][j] + A[i+1][j+1] > A[i+1][j] + A[i][j+1]:
                    print('No')
                    return
    print('Yes')

if __name__ == '__main__':
    main()