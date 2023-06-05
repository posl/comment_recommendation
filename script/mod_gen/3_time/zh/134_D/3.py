def check(a):
    for i in range(1, len(a) + 1):
        if a[i - 1] != 0 and a[i - 1] != 1:
            return False
    return True

if __name__ == '__main__':
    check()