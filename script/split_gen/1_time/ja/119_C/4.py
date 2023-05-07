def main():
    N, A, B, C = map(int, input().split())
    l = [int(input()) for _ in range(N)]
    print(dfs(0, 0, 0, 0))
