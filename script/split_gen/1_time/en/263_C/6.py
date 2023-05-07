def main():
    n, m = map(int, input().split())
    for i in range(1, m+1):
        dfs(i, 1, n, m)
