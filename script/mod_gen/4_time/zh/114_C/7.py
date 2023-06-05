def dfs(n, use):
    if n > N:
        return 0
    ret = 1 if use == 0b111 else 0
    ret += dfs(n * 10 + 3, use | 0b001)
    ret += dfs(n * 10 + 5, use | 0b010)
    ret += dfs(n * 10 + 7, use | 0b100)
    return ret
N = int(input())
print(dfs(0, 0))
