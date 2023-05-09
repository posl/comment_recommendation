def get_name(n):
    name = ''
    while n > 0:
        n -= 1
        name += chr(ord('a') + n % 26)
        n //= 26
    return name[::-1]
