def solve(h, w, a):
    min_a = 100
    for i in range(h):
        for j in range(w):
            min_a = min(min_a, a[i][j])
    ans = 0
    for i in range(h):
        for j in range(w):
            ans += a[i][j] - min_a
    return ans
