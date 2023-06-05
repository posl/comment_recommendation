def solve():
    H,W,A,B = map(int,input().split())
    #print(H,W,A,B)
    ans = 0
    def dfs(i,bit,used):
        if i == H*W:
            nonlocal ans
            ans += 1
            return
        if used>>i&1:
            dfs(i+1,bit,used)
            return
        if i%W != W-1 and not used>>(i+1)&1 and bit>>i&1 == bit>>(i+1)&1:
            dfs(i+1,bit,used|(1<<i)|(1<<(i+1)))
        if i+W < H*W and not used>>(i+W)&1 and bit>>i&1 == bit>>(i+W)&1:
            dfs(i+1,bit,used|(1<<i)|(1<<(i+W)))
        return
    dfs(0,0,(1<<(H*W))-1)
    print(ans)
    return
