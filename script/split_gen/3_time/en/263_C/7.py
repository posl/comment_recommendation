def main():
    n, m = map(int, input().split())
    for i in range(1, m + 1):
        dfs(n - 1, i, str(i))
