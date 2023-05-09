def solve(n, x, ab):
    ab.sort(key=lambda x: x[0] + x[1])
    t = 0
    for a, b in ab:
        t += a + b
        if t > x:
            return "No"
    return "Yes"
