def get_name(n):
    name = ""
    while n > 0:
        n -= 1
        name = chr(ord('a') + n % 26) + name
        n //= 26
    return name

if __name__ == '__main__':
    get_name()