def dfs(i, sum):
    if i == n:
        return sum == S
    if dfs(i + 1, sum):
        return True
    if dfs(i + 1, sum + a[i]):
        return True
    return False

if __name__ == '__main__':
    dfs()