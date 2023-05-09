def main():
    N, A, B, C = map(int, input().split())
    L = [int(input()) for i in range(N)]
    print(dfs(0, 0, 0, 0))
