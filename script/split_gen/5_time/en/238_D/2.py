def solve(a,s):
    if a > s:
        return "No"
    if (s-a)%2 == 0:
        return "Yes"
    else:
        return "No"
