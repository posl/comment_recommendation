def get_char(n, x):
    if n == 1:
        return chr(x + 64)
    elif x <= n:
        return chr(x + 64)
    else:
        return chr(x % n + 64)

if __name__ == '__main__':
    get_char()