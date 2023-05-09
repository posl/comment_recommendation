def get_char(n, x):
    if x <= n:
        return chr(64 + x)
    else:
        return get_char(n, x - n)

if __name__ == '__main__':
    get_char()