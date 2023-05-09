def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    for i in range(n):
        if s[i] in t:
            print(-1)
            exit()
    def dfs(i, j):
        if j == n:
            return ""
        for k in range(n):
            if i & (1 << k):
                continue
            if i == 0:
                ret = dfs(i | (1 << k), j + 1)
                if ret != "":
                    return s[k] + ret
            else:
                ret = dfs(i | (1 << k), j + 1)
                if ret != "":
                    return s[k] + "_" + ret
        return ""
    print(dfs(0, 0))
