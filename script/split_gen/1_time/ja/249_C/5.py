def main():
    N, K = map(int, input().split())
    S = [set(input()) for _ in range(N)]
    print(dfs(0, S, K, set()))
