def main():
    H, W, A, B = map(int, input().split())
    print(dfs(H, W, A, B))
