def solve(a,s):
    if a > s:
        return "No"
    if (a + s) % 2 == 1:
        return "No"
    if a == 0:
        return "Yes"
    if a == s:
        return "Yes"
    if a == 1 and s == 2:
        return "Yes"
    if a == 2 and s == 1:
        return "Yes"
    if a == 1 and s == 4:
        return "Yes"
    if a == 4 and s == 1:
        return "Yes"
    if a == 2 and s == 4:
        return "Yes"
    if a == 4 and s == 2:
        return "Yes"
    if a == 1 and s == 8:
        return "Yes"
    if a == 8 and s == 1:
        return "Yes"
    if a == 2 and s == 8:
        return "Yes"
    if a == 8 and s == 2:
        return "Yes"
    if a == 4 and s == 8:
        return "Yes"
    if a == 8 and s == 4:
        return "Yes"
    if a == 1 and s == 16:
        return "Yes"
    if a == 16 and s == 1:
        return "Yes"
    if a == 2 and s == 16:
        return "Yes"
    if a == 16 and s == 2:
        return "Yes"
    if a == 4 and s == 16:
        return "Yes"
    if a == 16 and s == 4:
        return "Yes"
    if a == 8 and s == 16:
        return "Yes"
    if a == 16 and s == 8:
        return "Yes"
    if a == 1 and s == 32:
        return "Yes"
    if a == 32 and s == 1:
        return "Yes"
    if a == 2 and s == 32:
        return "Yes"
    if a == 32 and s == 2:
        return "Yes"
    if a == 4 and s == 32:
        return "Yes"
    if a == 32 and s == 4:
        return "Yes"
