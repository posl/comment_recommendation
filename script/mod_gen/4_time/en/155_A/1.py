def is_poor(a, b, c):
    if a == b and b != c:
        return True
    elif a == c and b != c:
        return True
    elif b == c and a != c:
        return True
    else:
        return False

if __name__ == '__main__':
    is_poor()