def check(a, b, c):
    if a < b + c and b < c + a and c < a + b:
        return True
    return False

if __name__ == '__main__':
    check()