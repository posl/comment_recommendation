def solve():
    n,m = map(int,input().split())
    ans = [-1]*n
    for _ in range(m):
        a,b = map(int,input().split())
        if ans[a-1]==-1 and ans[b-1]==-1:
            ans[a-1]=b
            ans[b-1]=a
        elif ans[a-1]==-1:
            ans[a-1]=b
            ans[b-1]=a
        elif ans[b-1]==-1:
            ans[b-1]=a
            ans[a-1]=b
        else:
            if ans[a-1]==b:
                continue
            else:
                print(-1)
                return
    print(*ans)
solve()

if __name__ == '__main__':
    solve()