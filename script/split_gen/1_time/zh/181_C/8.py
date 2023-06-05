def is_same_line(p1, p2, p3):
    if p1[0] == p2[0] and p2[0] == p3[0]:
        return True
    if p1[1] == p2[1] and p2[1] == p3[1]:
        return True
    if p1[0] == p2[0] or p1[1] == p2[1]:
        return False
    if p1[0] == p3[0] or p1[1] == p3[1]:
        return False
    if p2[0] == p3[0] or p2[1] == p3[1]:
        return False
    if (p1[0] - p2[0]) * (p1[1] - p3[1]) == (p1[0] - p3[0]) * (p1[1] - p2[1]):
        return True
    else:
        return False
