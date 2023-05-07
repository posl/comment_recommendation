def main():
    #read
    H, W = map(int, input().split())
    grid = [list(input()) for _ in range(H)]
    #solve
    ans = [0]*W
    for j in range(W):
        for i in range(H):
            if grid[i][j] == "#":
                ans[j] += 1
    #print
    print(*ans)
