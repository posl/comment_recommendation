def is_median(a, b, c):
    if b > a and b < c:
        return True
    elif b < a and b > c:
        return True
    else:
        return False

if __name__ == '__main__':
    is_median()