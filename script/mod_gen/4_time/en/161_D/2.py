def lunlun(n):
    if n < 10:
        return True
    d = n % 10
    n //= 10
    while n > 0:
        if abs(n % 10 - d) > 1:
            return False
        d = n % 10
        n //= 10
    return True

if __name__ == '__main__':
    lunlun()