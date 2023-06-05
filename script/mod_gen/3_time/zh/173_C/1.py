def solve(h,w,k,grid):
    ans = 0
    for i in range(2**h):
        for j in range(2**w):
            cnt = 0
            for r in range(h):
                for c in range(w):
                    if ((i>>r)&1)==0 and ((j>>c)&1)==0 and grid[r][c]=='#':
                        cnt += 1
            if cnt==k:
                ans += 1
    return ans

if __name__ == '__main__':
    solve()