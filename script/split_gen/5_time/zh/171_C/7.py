def get_name(n):
    name = ''
    while n > 0:
        n -= 1
        name = chr(n % 26 + ord('a')) + name
        n = n // 26
    return name
