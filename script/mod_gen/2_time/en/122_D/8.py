def dfs(n, s):
    global ans, MOD
    if n == 0:
        ans += 1
        return
    for c in "ACGT":
        if s[-1:] + c in ["AGC", "GAC", "ACG"]:
            continue
        dfs(n - 1, s[-2:] + c)

if __name__ == '__main__':
    dfs()