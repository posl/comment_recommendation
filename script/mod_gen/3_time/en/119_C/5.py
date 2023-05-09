def main():
    N, A, B, C = map(int, input().split())
    L = [int(input()) for _ in range(N)]
    ans = float('inf')
    def dfs(cur, a, b, c):
        nonlocal ans
        if cur == N:
            if min(a, b, c) > 0:
                ans = min(ans, abs(a - A) + abs(b - B) + abs(c - C) - 30)
            return
        dfs(cur + 1, a, b, c)
        dfs(cur + 1, a + L[cur], b, c) + 10
        dfs(cur + 1, a, b + L[cur], c) + 10
        dfs(cur + 1, a, b, c + L[cur]) + 10
    dfs(0, 0, 0, 0)
    print(ans)

if __name__ == '__main__':
    main()