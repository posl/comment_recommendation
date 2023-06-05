def solve(a, s):
    if a > s:
        return False
    if (s - a) % 2 == 0:
        return True
    return False
