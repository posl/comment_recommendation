def get_char(n, x):
    if x % n == 0:
        return chr(64 + n)
    else:
        return chr(64 + x % n)

if __name__ == '__main__':
    get_char()