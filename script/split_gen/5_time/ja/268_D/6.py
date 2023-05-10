def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    def check(x):
        for ti in t:
            if x.find(ti) >= 0:
                return False
        return True
    def dfs(i, x):
        if i == n:
            return x
        for j in range(i, n):
            if dfs(j + 1, x + s[j]) is not None:
                return x
        return None
    def solve():
        for i in range(n):
            x = dfs(i + 1, s[i])
            if x is not None and check(x):
                return x
        return None
    ans = solve()
    if ans is None:
        print(-1)
    else:
        print(ans)
