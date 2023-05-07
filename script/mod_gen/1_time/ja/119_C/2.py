def dfs(i, a, b, c):
    global ans
    if i == n:
        if min(a, b, c) > 0:
            ans = min(ans, abs(a - A) + abs(b - B) + abs(c - C) - 30)
        return
    dfs(i + 1, a, b, c)
    dfs(i + 1, a + l[i], b, c)
    dfs(i + 1, a, b + l[i], c)
    dfs(i + 1, a, b, c + l[i])
n, A, B, C = map(int, input().split())
l = [int(input()) for i in range(n)]
ans = 10**9
dfs(0, 0, 0, 0)
print(ans)

if __name__ == '__main__':
    dfs()