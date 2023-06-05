def get_min_step(r1, c1, r2, c2):
    if r1 == r2 and c1 == c2:
        return 0
    if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
        return 1
    if (r1 - r2 + c1 - c2) % 2 == 0:
        return 2
    return 3
