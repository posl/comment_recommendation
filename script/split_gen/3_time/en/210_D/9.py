def main():
    H,W,C = map(int,input().split())
    A = [list(map(int,input().split())) for _ in range(H)]
    #マス(1,1)からマス(i,j)までの最小コスト
    min_cost = [[0] * W for _ in range(H)]
    min_cost[0][0] = A[0][0]
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                min_cost[i][j] = min(min_cost[i][j-1],A[i][j])
            elif j == 0:
                min_cost[i][j] = min(min_cost[i-1][j],A[i][j])
            else:
                min_cost[i][j] = min(min_cost[i-1][j],min_cost[i][j-1],A[i][j])
    #マス(H,W)からマス(i,j)までの最小コスト
    min_cost2 = [[0] * W for _ in range(H)]
    min_cost2[H-1][W-1] = A[H-1][W-1]
    for i in range(H-1,-1,-1):
        for j in range(W-1,-1,-1):
            if i == H-1 and j == W-1:
                continue
            elif i == H-1:
                min_cost2[i][j] = min(min_cost2[i][j+1],A[i][j])
            elif j == W-1:
                min_cost2[i][j] = min(min_cost2[i+1][j],A[i][j])
            else:
                min_cost2[i][j] = min(min_cost2[i+1][j],min_cost2[i][j+1],A[i][j])
    #マス(1,1)からマス(i,j)までの最小コスト + マス(H,W)からマス(i,j)までの最小コスト - A[i][j] + C
    ans = float("inf")
    for i in range(H):
        for j in range(W):
            ans = min(ans,min_cost[i][j] + min_cost2[i][j] - A[i][
