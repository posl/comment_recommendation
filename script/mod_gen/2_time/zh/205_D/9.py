def compare_pow(a, b, c):
    if pow(a, c) < pow(b, c):
        return '<'
    elif pow(a, c) > pow(b, c):
        return '>'
    else:
        return '='

if __name__ == '__main__':
    compare_pow()