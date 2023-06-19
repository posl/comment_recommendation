def maze():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '.':
                ans += 1
    if ans == h * w:
        return ans - 1
    else:
        return ans
print(maze())
