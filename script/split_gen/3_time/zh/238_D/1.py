def solve(a, s):
    if s < a:
        return False
    if (s - a) % 2 == 0:
        return True
    else:
        return False
