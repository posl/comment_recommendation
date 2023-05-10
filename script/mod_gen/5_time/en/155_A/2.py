def is_poor(a, b, c):
    if a == b and a != c:
        return True
    if a == c and a != b:
        return True
    if b == c and a != b:
        return True
    return False

if __name__ == '__main__':
    is_poor()