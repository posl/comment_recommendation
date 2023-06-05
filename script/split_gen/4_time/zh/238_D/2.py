def solve(a, s):
    if s < a:
        return False
    if (s - a) & a == 0:
        return True
    return False
