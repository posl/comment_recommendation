def get_min_count(n):
    count = 0
    while n != 0:
        if n >= 729:
            n -= 729
            count += 1
        elif n >= 216:
            n -= 216
            count += 1
        elif n >= 81:
            n -= 81
            count += 1
        elif n >= 36:
            n -= 36
            count += 1
        elif n >= 9:
            n -= 9
            count += 1
        elif n >= 6:
            n -= 6
            count += 1
        elif n >= 1:
            n -= 1
            count += 1
    return count

if __name__ == '__main__':
    get_min_count()