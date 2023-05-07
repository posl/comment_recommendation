def is_full_house(a, b, c, d, e):
    # write your code here
    return "Yes" if (a == b == c and d == e) or (a == b and c == d == e) else "No"
