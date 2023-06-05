def hamburger(n, x):
    if n == 0:
        return 0 if x <= 0 else 1
    elif x <= 1 + hamburger(n - 1, n - 1):
        return hamburger(n - 1, x - 1)
    else:
        return 1 + n + hamburger(n - 1, x - 2 - hamburger(n - 1, n - 1))

if __name__ == '__main__':
    hamburger()