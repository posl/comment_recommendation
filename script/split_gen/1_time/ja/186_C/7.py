def check(n):
    while n > 0:
        if n % 10 == 7:
            return False
        n //= 10
    return True
