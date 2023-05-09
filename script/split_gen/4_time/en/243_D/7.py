def main():
    import sys
    sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    N, X = map(int, input().split())
    S = input().rstrip()
    def dfs(n, x):
        if n == 0:
            return x
        elif S[n - 1] == 'U':
            return dfs(n - 1, x)
        elif S[n - 1] == 'L':
            return dfs(n - 1, x * 2)
        else:
            return dfs(n - 1, x * 2 + 1)
    print(dfs(N, X))
