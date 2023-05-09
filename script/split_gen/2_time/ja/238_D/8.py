def solve(a,s):
    if a > s:
        return "No"
    elif a == s:
        return "Yes"
    elif (s - a) % 2 == 0:
        return "Yes"
    else:
        return "No"
