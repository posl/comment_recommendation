def solve():
    #import sys
    #input = sys.stdin.readline
    N = int(input())
    ans = 0
    def dfs(s):
        nonlocal ans
        if int(s) > N:
            return
        if all(s.count(c) > 0 for c in '753'):
            ans += 1
        for c in '753':
            dfs(s + c)
    dfs('0')
    print(ans)
