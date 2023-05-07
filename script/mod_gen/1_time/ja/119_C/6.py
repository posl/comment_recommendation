def dfs(now, a, b, c, mp):
    global ans
    if now == N:
        if min(a, b, c) > 0:
            ans = min(ans, mp + abs(a - A) + abs(b - B) + abs(c - C))
        return
    dfs(now + 1, a, b, c, mp)
    dfs(now + 1, a + l[now], b, c, mp + 10 * (a > 0))
    dfs(now + 1, a, b + l[now], c, mp + 10 * (b > 0))
    dfs(now + 1, a, b, c + l[now], mp + 10 * (c > 0))
N, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(N)]
ans = 10 ** 10
dfs(0, 0, 0, 0, 0)
print(ans)
問題文
高橋君��

if __name__ == '__main__':
    dfs()