def check(n, m, a, b, c, d):
    for i in range(n):
        if (a[i] in c) and (b[i] in d):
            pass
        elif (a[i] in d) and (b[i] in c):
            pass
        else:
            return False
    return True

if __name__ == '__main__':
    check()