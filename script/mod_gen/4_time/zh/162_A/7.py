def has_seven(n):
    while n > 0:
        if n % 10 == 7:
            return True
        n //= 10
    return False

if __name__ == '__main__':
    has_seven()