def poor(a, b, c):
    if a == b and b != c:
        return True
    elif a == c and a != b:
        return True
    elif b == c and b != a:
        return True
    else:
        return False

if __name__ == '__main__':
    poor()