def dfs(h,w,board,cnt):
    global ans
    ans = max(ans,cnt)
    for i in range(h):
        for j in range(w):
            if board[i][j] == '.':
                board[i][j] = '#'
                if i > 0 and board[i-1][j] == '.':
                    dfs(h,w,board,cnt+1)
                if i < h-1 and board[i+1][j] == '.':
                    dfs(h,w,board,cnt+1)
                if j > 0 and board[i][j-1] == '.':
                    dfs(h,w,board,cnt+1)
                if j < w-1 and board[i][j+1] == '.':
                    dfs(h,w,board,cnt+1)
                board[i][j] = '.'
