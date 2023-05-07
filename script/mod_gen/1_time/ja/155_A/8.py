def check(a, b, c):
    if a == b:
        if a != c:
            return True
        else:
            return False
    elif b == c:
        if b != a:
            return True
        else:
            return False
    elif c == a:
        if c != b:
            return True
        else:
            return False
    else:
        return False

if __name__ == '__main__':
    check()