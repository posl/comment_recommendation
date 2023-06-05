def check(a,b):
    if a[0] == b[0] or a[0] == b[1] or a[1] == b[0] or a[1] == b[1]:
        return True
    else:
        return False

if __name__ == '__main__':
    check()