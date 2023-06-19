def solve():
    N,M = map(int,input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    ans = dfs(S,T,0)
    print(ans)

if __name__ == '__main__':
    solve()