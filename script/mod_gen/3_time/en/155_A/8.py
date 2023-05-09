def checkPoor(a, b, c):
    if a == b and a != c:
        return True
    elif b == c and b != a:
        return True
    elif a == c and a != b:
        return True
    else:
        return False

if __name__ == '__main__':
    checkPoor()