def check753(n):
    if n < 357:
        return False
    if n % 7 == 0 or n % 5 == 0 or n % 3 == 0:
        return False
    if '7' not in str(n) or '5' not in str(n) or '3' not in str(n):
        return False
    return True

if __name__ == '__main__':
    check753()