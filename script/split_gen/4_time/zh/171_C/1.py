def dog_name(n):
    name = ''
    while n > 0:
        n -= 1
        name += chr(n % 26 + ord('a'))
        n //= 26
    return name[::-1]
