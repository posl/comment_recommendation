def is_middle(a, b, c):
    if (a <= b and b <= c) or (c <= b and b <= a):
        return True
    else:
        return False

if __name__ == '__main__':
    is_middle()