def get_length(l1, r1, l2, r2):
    if (r1 < l2) or (r2 < l1):
        return 0
    else:
        return min(r1, r2) - max(l1, l2)

if __name__ == '__main__':
    get_length()