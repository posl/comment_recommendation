def main():
    h,w = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    #print(s)
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '.':
                #print(i,j)
                t = [[-1]*w for _ in range(h)]
                t[i][j] = 0
                q = [(i,j)]
                while q:
                    x,y = q.pop(0)
                    for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                        nx,ny = x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and s[nx][ny]=='.' and t[nx][ny]==-1:
                            t[nx][ny] = t[x][y] + 1
                            q.append((nx,ny))
                ans = max(ans, max([max(i) for i in t]))
    print(ans)

if __name__ == '__main__':
    main()