def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                continue
            if i == 0:
                A[i][j] += A[i][j-1]
            elif j == 0:
                A[i][j] += A[i-1][j]
            else:
                A[i][j] += min(A[i-1][j], A[i][j-1])
    
    for i in range(H):
        for j in range(W):
            if i == H-1 and j == W-1:
                continue
            if i == H-1:
                A[i][j] -= A[i][j+1]
            elif j == W-1:
                A[i][j] -= A[i+1][j]
            else:
                A[i][j] -= max(A[i+1][j], A[i][j+1])
    
    for i in range(H):
        for j in range(W):
            if A[i][j] > 0:
                print('Yes')
                return
    print('No')
    return

if __name__ == '__main__':
    main()