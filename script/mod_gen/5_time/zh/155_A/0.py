def is_diff(a, b, c):
    if a == b and b != c:
        return True
    elif a == c and c != b:
        return True
    elif b == c and c != a:
        return True
    else:

if __name__ == '__main__':
    is_diff()