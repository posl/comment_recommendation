def dfs(depth, a, b, c):
    global ans
    if depth == n:
        if a and b and c:
            ans = min(ans, abs(a - A) + abs(b - B) + abs(c - C) - 30)
        return
    dfs(depth + 1, a, b, c)
    dfs(depth + 1, a + l[depth], b, c)
    dfs(depth + 1, a, b + l[depth], c)
    dfs(depth + 1, a, b, c + l[depth])
n, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(n)]
ans = float("inf")
dfs(0, 0, 0, 0)
print(ans)

if __name__ == '__main__':
    dfs()