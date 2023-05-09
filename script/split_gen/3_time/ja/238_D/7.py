def solve(a, s):
    if a > s:
        return False
    if s % 2 == 0 and a % 2 == 0:
        return True
    if s % 2 == 1 and a % 2 == 1:
        return True
    return False
