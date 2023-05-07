def main():
    H, W = map(int, input().split())
    G = [input() for _ in range(H)]
    ans = [1, 1]
    for _ in range(H*W):
        i, j = ans[0]-1, ans[1]-1
        if G[i][j] == "U":
            if i == 0:
                break
            ans[0] -= 1
        elif G[i][j] == "D":
            if i == H-1:
                break
            ans[0] += 1
        elif G[i][j] == "L":
            if j == 0:
                break
            ans[1] -= 1
        elif G[i][j] == "R":
            if j == W-1:
                break
            ans[1] += 1
    else:
        ans = [-1]
    print(*ans)
