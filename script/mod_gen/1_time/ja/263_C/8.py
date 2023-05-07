def dfs(n,m,k,ans):
    if k==n:
        print(' '.join(map(str,ans)))
        return
    for i in range(ans[-1],m+1):
        ans.append(i)
        dfs(n,m,k+1,ans)
        ans.pop()

if __name__ == '__main__':
    dfs()