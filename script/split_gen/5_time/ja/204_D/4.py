def solve(n, t):
    t.sort(reverse=True)
    oven1 = 0
    oven2 = 0
    for i in range(n):
        if oven1 <= oven2:
            oven1 += t[i]
        else:
            oven2 += t[i]
    return max(oven1, oven2)
