def solve():
    n,m = list(map(int, input().split()))
    ans = []
    def dfs(a):
        if len(a) == n:
            ans.append(a)
            return
        for i in range(1, m+1):
            if a[-1] < i:
                dfs(a+[i])
    for i in range(1, m+1):
        dfs([i])
    for a in ans:
        print(*a)
solve()

if __name__ == '__main__':
    solve()