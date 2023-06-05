def dfs(a, b, c, mp, l, n, i):
    if i == n:
        if a == 0 or b == 0 or c == 0:
            return 10**9
        else:
            return mp - 30
    else:
        mp1 = dfs(a, b, c, mp, l, n, i + 1)
        mp2 = dfs(a - l[i], b, c, mp + 10, l, n, i + 1)
        mp3 = dfs(a, b - l[i], c, mp + 10, l, n, i + 1)
        mp4 = dfs(a, b, c - l[i], mp + 10, l, n, i + 1)
        return min(mp1, mp2, mp3, mp4)
n, a, b, c = map(int, input().split())
l = [int(input()) for _ in range(n)]
print(dfs(a, b, c, 0, l, n, 0))
