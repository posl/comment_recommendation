def solve(a, s):
    if s < a:
        return False
    if s % 2 != a % 2:
        return False
    return True
