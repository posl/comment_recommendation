def dfs(i,j,black):
    if i == H:
        if black == K:
            return 1
        else:
            return 0
    if j == W:
        return dfs(i+1,0,black)
    ret = 0
    ret += dfs(i,j+1,black)
    ret += dfs(i,j+1,black+1)
    return ret
H,W,K = map(int,input().split())
c = [list(input()) for _ in range(H)]
print(dfs(0,0,0))
