def get_score(a, b):
    if a == 'G' and b == 'C':
        return 1
    if a == 'C' and b == 'P':
        return 1
    if a == 'P' and b == 'G':
        return 1
    if a == b:
        return 0
    return -1
