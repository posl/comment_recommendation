def is_included_seven(n):
    while n != 0:
        if n % 10 == 7:
            return True
        n //= 10
    return False
n = int(input())
