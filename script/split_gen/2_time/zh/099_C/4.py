def get_min_count(N):
    count = 0
    while N > 0:
        if N >= 729:
            N -= 729
        elif N >= 216:
            N -= 216
        elif N >= 81:
            N -= 81
        elif N >= 36:
            N -= 36
        elif N >= 9:
            N -= 9
        elif N >= 6:
            N -= 6
        elif N >= 1:
            N -= 1
        count += 1
    return count
