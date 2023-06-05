def find_min_count(n):
    count = 0
    while n > 0:
        if n >= 729:
            n -= 729
        elif n >= 216:
            n -= 216
        elif n >= 81:
            n -= 81
        elif n >= 36:
            n -= 36
        elif n >= 9:
            n -= 9
        elif n >= 6:
            n -= 6
        else:
            n -= 1
        count += 1
    return count
