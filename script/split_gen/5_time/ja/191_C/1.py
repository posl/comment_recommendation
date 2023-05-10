def main():
    H,W = map(int,input().split())
    S = [list(input()) for _ in range(H)]
    cnt = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                cnt += 1
    if cnt == 0:
        print(0)
        return
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                ans += 1
                stack = [(i,j)]
                while stack:
                    x,y = stack.pop()
                    if 0 <= x-1 and S[x-1][y] == "#":
                        stack.append((x-1,y))
                        S[x-1][y] = "."
                    if x+1 < H and S[x+1][y] == "#":
                        stack.append((x+1,y))
                        S[x+1][y] = "."
                    if 0 <= y-1 and S[x][y-1] == "#":
                        stack.append((x,y-1))
                        S[x][y-1] = "."
                    if y+1 < W and S[x][y+1] == "#":
                        stack.append((x,y+1))
                        S[x][y+1] = "."
    print(ans)
    return
