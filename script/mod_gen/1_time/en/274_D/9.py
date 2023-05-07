def check(x, y, a):
    for i in range(1, len(a)):
        if a[i] == abs(x) + abs(y):
            return True
    return False

if __name__ == '__main__':
    check()