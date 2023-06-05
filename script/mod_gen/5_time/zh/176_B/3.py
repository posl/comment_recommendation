def is_9_multiple(n):
    if n == 0:
        return True
    if n % 9 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    is_9_multiple()