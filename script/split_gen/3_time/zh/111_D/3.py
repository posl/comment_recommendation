def get_direction(x, y, x1, y1):
    if x == x1 and y == y1:
        return ""
    if x == x1:
        if y1 > y:
            return "U"
        else:
            return "D"
    elif y == y1:
        if x1 > x:
            return "R"
        else:
            return "L"
    else:
        return ""
