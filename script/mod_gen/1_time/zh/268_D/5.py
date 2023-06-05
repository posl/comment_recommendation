def solve(n, m, s, t):
    def ok(x):
        if len(x) < 3 or len(x) > 16:
            return False
        for i in range(m):
            if t[i] in x:
                return False
        return True
    def dfs(i, x):
        if i == n:
            if ok(x):
                return x
            else:
                return ""
        for j in range(n):
            if not used[j]:
                used[j] = True
                res = dfs(i + 1, x + s[j])
                if res != "":
                    return res
                used[j] = False
        return ""
    used = [False] * n
    return dfs(0, "")
n, m = map(int, input().split())
s = [input() for i in range(n)]
t = [input() for i in range(m)]
print(solve(n, m, s, t))
