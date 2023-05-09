def main():
    N, A, B, C = map(int, input().split())
    L = [int(input()) for i in range(N)]
    ans = 10**9
    def dfs(i, a, b, c):
        nonlocal ans
        if i == N:
            if min(a, b, c) > 0:
                ans = min(ans, abs(a - A) + abs(b - B) + abs(c - C) - 30)
            return
        dfs(i + 1, a, b, c)
        dfs(i + 1, a + L[i], b, c) + 10
        dfs(i + 1, a, b + L[i], c) + 10
        dfs(i + 1, a, b, c + L[i]) + 10
    dfs(0, 0, 0, 0)
    print(ans)
