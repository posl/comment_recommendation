def check(n):
    if n % 2 == 0 and (n % 3 == 0 or n % 5 == 0):
        return True
    else:
        return False

if __name__ == '__main__':
    check()