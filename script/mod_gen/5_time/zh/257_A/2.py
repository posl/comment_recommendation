def get_char(n, x):
    char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return char[(x - 1) % 26]

if __name__ == '__main__':
    get_char()