def solve(a,b,x):
    if x == a * a * b:
        return 0
    if x > a * a * b / 2:
        return 90 - solve(a,b,a * a * b - x)
    return solve(b,a * a * b - x,b * b * a)
