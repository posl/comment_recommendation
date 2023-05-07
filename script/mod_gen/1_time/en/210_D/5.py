def main():
    H,W,C = map(int,input().split())
    A = [list(map(int,input().split())) for _ in range(H)]
    min_A = [[10**9]*W for _ in range(H)]
    min_A[0][0] = A[0][0]
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                continue
            if i == 0:
                min_A[i][j] = min(min_A[i][j-1],A[i][j])
            elif j == 0:
                min_A[i][j] = min(min_A[i-1][j],A[i][j])
            else:
                min_A[i][j] = min(min_A[i-1][j],min_A[i][j-1],A[i][j])
    max_A = [[0]*W for _ in range(H)]
    max_A[H-1][W-1] = A[H-1][W-1]
    for i in range(H-1,-1,-1):
        for j in range(W-1,-1,-1):
            if i == H-1 and j == W-1:
                continue
            if i == H-1:
                max_A[i][j] = max(max_A[i][j+1],A[i][j])
            elif j == W-1:
                max_A[i][j] = max(max_A[i+1][j],A[i][j])
            else:
                max_A[i][j] = max(max_A[i+1][j],max_A[i][j+1],A[i][j])
    ans = 10**18
    for i in range(H):
        for j in range(W):
            ans = min(ans,min_A[i][j]+max_A[i][j]+C*(i+j))
    print(ans)

if __name__ == '__main__':
    main()