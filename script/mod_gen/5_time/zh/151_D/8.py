def main():
    h,w = map(int,input().split())
    s = [list(input()) for _ in range(h)]
    def dfs(i,j):
        s[i][j] = "#"
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            ni,nj = i+dx,j+dy
            if ni < 0 or ni >= h or nj < 0 or nj >= w:
                continue
            if s[ni][nj] == "#":
                continue
            dfs(ni,nj)
        s[i][j] = "."
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                continue
            t = [[0]*w for _ in range(h)]
            t[i][j] = 1
            q = [(i,j)]
            while q:
                ni,nj = q.pop(0)
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    x,y = ni+dx,nj+dy
                    if x < 0 or x >= h or y < 0 or y >= w:
                        continue
                    if s[x][y] == "#":
                        continue
                    if t[x][y] > 0:
                        continue
                    t[x][y] = t[ni][nj] + 1
                    q.append((x,y))
            for k in range(h):
                for l in range(w):
                    if s[k][l] == "#":
                        continue
                    ans = max(ans,t[k][l]-1)
    print(ans)

if __name__ == '__main__':
    main()