def dfs(a, b, k):
    if a == 0:
        return 'b' * b
    if b == 0:
        return 'a' * a
    num = comb[a + b - 1][b]
    if k <= num:
        return 'a' + dfs(a - 1, b, k)
    else:
        return 'b' + dfs(a, b - 1, k - num)

if __name__ == '__main__':
    dfs()