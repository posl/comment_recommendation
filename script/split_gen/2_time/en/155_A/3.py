def poor(a, b, c):
    if (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
        return "Yes"
    else:
        return "No"
