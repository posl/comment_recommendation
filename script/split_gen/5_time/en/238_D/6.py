def solve(a, s):
    if a == s:
        return "Yes"
    if a > s:
        return "No"
    if a == 0:
        return "No"
    if (s - a) % 2 == 0:
        return "Yes"
    return "No"
