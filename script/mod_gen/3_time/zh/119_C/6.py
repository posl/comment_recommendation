def dfs(i, a, b, c, mp):
    global ans
    if i == n:
        if min(a, b, c) > 0:
            ans = min(ans, mp + abs(a - A) + abs(b - B) + abs(c - C) - 30)
        return
    dfs(i + 1, a, b, c, mp)
    dfs(i + 1, a + l[i], b, c, mp + 10)
    dfs(i + 1, a, b + l[i], c, mp + 10)
    dfs(i + 1, a, b, c + l[i], mp + 10)
n, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(n)]
ans = float("inf")
dfs(0, 0, 0, 0, 0)
print(ans)

if __name__ == '__main__':
    dfs()