def solve(h, w, a):
    min_a = min([min(row) for row in a])
    return sum([sum([a[i][j] - min_a for j in range(w)]) for i in range(h)])
